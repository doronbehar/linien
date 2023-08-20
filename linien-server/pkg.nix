{ lib
, buildPythonPackage
, version
, src
, setuptools
, importlib-metadata
, cma
, fire
, pylpsd
, pyrp3
, rpyc
, influxdb-client
, linien-common
}:

buildPythonPackage {
  pname = "linien-server";
  inherit version;
  pyproject = true;

  inherit src;

  nativeBuildInputs = [
    setuptools
    importlib-metadata
  ];

  propagatedBuildInputs = [
    cma
    fire
    influxdb-client
    pylpsd
    pyrp3
    rpyc
    linien-common
  ];

  # The linien-server executable provides an `enable` subcommand that installs
  # the service file to /etc/systemd/system (hardcoded). We do this so that the
  # service could be enabled by debian builder at ../flake.nix .
  postInstall = ''
    install -Dm0644 \
      ./linien_server/linien-server.service \
      $out/lib/systemd/system/linien-server.service
  '';

  # Same issue as explained in ../linien-common/pkg.nix
  preBuild = ''
    export HOME="$(mktemp -d)"
  '';

  pythonImportsCheck = [
    "linien_server"
  ];

  meta = with lib; {
    description = "Server components of the Linien spectroscopy lock application";
    homepage = "https://github.com/linien-org/linien";
    license = licenses.gpl3;
  };
}
