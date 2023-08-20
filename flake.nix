{
  description = "Spectroscopy lock application using RedPitaya";

  # Updating this triggers a lot of rebuilds, since scipy has many dependents,
  # prepare yourself before updating.
  # Needs my fork for: https://github.com/NixOS/nixpkgs/pull/330928
  inputs.nixpkgs.url = "github:doronbehar/nixpkgs/pkg/misoc";
  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.gitignore = {
    url = "github:hercules-ci/gitignore.nix";
    # Use the same nixpkgs
    inputs.nixpkgs.follows = "nixpkgs";
  };
  inputs.pyrp3 = {
    url = "github:linien-org/pyrp3/v2.0.1";
    flake = false;
  };

  outputs = { self
    , nixpkgs
    , flake-utils
    , gitignore
    , ...
  }@otherInputs:
  flake-utils.lib.eachDefaultSystem (system:
    let
      # Credit @kranzes <3: https://github.com/NixOS/nix/issues/8163#issuecomment-1517774089
      flakeDate2human = flakeInput: builtins.concatStringsSep "-" (builtins.match "(.{4})(.{2})(.{2}).*" flakeInput.lastModifiedDate);
      lockFile = builtins.fromJSON (builtins.readFile ./flake.lock);
      pkgs = import nixpkgs {
        inherit system;
      };
      inherit (pkgs) lib;
      pythonDevEnv = (python.withPackages(ps: builtins.attrValues {
        inherit (ps)
        click
        fire
        cma
        matplotlib
        migen
        misoc
        myhdl
        numpy
        paramiko
        plumbum
        pylpsd
        pyqt5
        pyqtgraph
        pyrp3
        pytest
        pytest-plt
        rpyc
        superqt
        scipy # From our fork
        # For text editor
        jedi-language-server
        debugpy
        # For testing installations
        setuptools
        setuptools-scm
        ;
      })).overrideAttrs (old: {
        meta = old.meta // {
          description = "Linien Python development environment";
        };
      });
      inherit (gitignore.lib) gitignoreFilterWith;
      get-local-src = subdirectory: lib.cleanSourceWith {
        filter = gitignoreFilterWith {
          basePath = ./.;
          extraRules = ''
            flake*
          '';
        };
        src = "${self}/${subdirectory}";
      };
      get-github-src-version = pname: {
        src = pkgs.fetchFromGitHub {
          inherit (lockFile.nodes.${pname}.original)
            owner
            repo
          ;
          sha256 = lockFile.nodes.${pname}.locked.narHash;
          rev = lockFile.nodes.${pname}.locked.rev;
        };
        version = if (builtins.hasAttr "ref" lockFile.nodes.${pname}.original) then
          lockFile.nodes.${pname}.original.ref
        else
          flakeDate2human otherInputs.${pname}
        ;
      };
      linienBuildArgs = {
        version = (builtins.fromTOML (builtins.readFile ./linien-server/pyproject.toml)).project.version;
      };
      # Generate a `python` interpreter, with some python packages overriden
      # and added - we merge the pythonOverrides of scipy-fork as well. We use
      # lib.composeExtensions as instructed here:
      # https://github.com/NixOS/nixpkgs/issues/44426
      pythonOverrides = lib.composeExtensions
        # Empty override, may be useful in the future
        (selfPython: superPython: {})
        (selfPython: superPython: {
          linien-gui = superPython.python.pkgs.callPackage ./linien-gui/pkg.nix (linienBuildArgs // {
            src = get-local-src "linien-gui";
            inherit (selfPython)
              linien-client
              pyqtgraph
            ;
          });
          linien-client = superPython.python.pkgs.callPackage ./linien-client/pkg.nix (linienBuildArgs // {
            src = get-local-src "linien-client";
            inherit (selfPython)
              linien-common
            ;
          });
          linien-common = superPython.python.pkgs.callPackage ./linien-common/pkg.nix (linienBuildArgs // {
            src = get-local-src "linien-common";
          });
          linien-server = superPython.python.pkgs.callPackage ./linien-server/pkg.nix (linienBuildArgs // {
            src = get-local-src "linien-server";
            inherit (selfPython)
              linien-common
              pylpsd
              pyrp3
            ;
          });
          pyrp3 = superPython.python.pkgs.callPackage
            ./pyrp3
            (get-github-src-version "pyrp3")
          ;
        })
      ;
      python = (pkgs.python3.override {
        packageOverrides = pythonOverrides;
      }).overrideAttrs(old: {
        meta = old.meta // {
          description = "Python interpreter with .pkgs set including linien";
        };
      });
      python-armv7l-hf-multiplatform = (pkgs.pkgsCross.armv7l-hf-multiplatform.python3.override {
        packageOverrides = pythonOverrides;
      }).overrideAttrs(old: {
        meta = old.meta // {
          description = "Python interpreter (cross compiled) with .pkgs set including linien";
        };
      });
      buildDeb = {pkg, targetArch, pkgName ? pkg.name}: pkgs.stdenv.mkDerivation {
        name = "${pkg.name}.deb";
        buildInputs = [
          pkgs.dpkg
        ];
        unpackPhase = "true";
        buildPhase = ''
          export HOME=$PWD
          mkdir -p pkgtree/nix/store/
          for item in "$(cat ${pkgs.referencesByPopularity pkg})"; do
            cp -r $item pkgtree/nix/store/
          done

          mkdir -p pkgtree/bin
          cp -r ${pkg}/bin/* pkgtree/bin/
          # We want Systemd files to be integrated with the target OS Systemd
          if [[ -d ${pkg}/lib/systemd ]]; then
            mkdir -p pkgtree/lib
            cp -r ${pkg}/lib/systemd pkgtree/lib/
          fi

          chmod -R a+rwx pkgtree/nix
          chmod -R a+rwx pkgtree/bin
          mkdir pkgtree/DEBIAN
          cat << EOF > pkgtree/DEBIAN/control
          Package: ${pkgName}
          Version: ${pkg.version}
          Maintainer: "github.com/bleykauf"
        ''
        # TODO: Ideally we would parse `pkgs.stdenv.gcc.arch` or a similar
        # attribute and use this argument such that dpkg-deb will be
        # satisfied with our name of the platform.
        + ''
          Architecture: ${targetArch}
          Description: ${pkg.meta.description}
          EOF
        '';
        installPhase = ''
          dpkg-deb -b pkgtree
          mv pkgtree.deb $out
        '';
        meta = {
          description = "Debian package of ${pkg.name} compiled for architecture ${targetArch}";
        };
      };
    in {
      devShells = {
        default = pkgs.mkShell {
          nativeBuildInputs = [
            pythonDevEnv
            # To inspect deb packages we build, using:
            #
            #    dpkg --contents $(nix build --print-out-paths -L .\#linien-server-deb-armv7l-hf-multiplatform)`
            pkgs.dpkg
            # To manage linien.bin
            pkgs.git-lfs
          ];
        };
      };
      packages = {
        # Put it here so it'll be easy to run commands such as:
        #
        #    nix why-depends --all --derivation .\#python.pkgs.linien-gui .\#nixpkgs-python.pkgs.scipy
        #
        nixpkgs-python = pkgs.python3;
        inherit pythonDevEnv;
        # The server is built for debian only, so we don't inherit it here
        inherit (python.pkgs)
          linien-common
          linien-client
          linien-gui
        ;
        inherit
          python
          python-armv7l-hf-multiplatform
        ;
        linien-server-deb-armv7l-hf-multiplatform = buildDeb {
          pkg = python-armv7l-hf-multiplatform.pkgs.linien-server;
          targetArch = "armhf";
          pkgName = "linien-server";
        };
      };
    }
  );
}
