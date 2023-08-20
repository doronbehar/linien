{ lib
, buildPythonPackage
, version
, src
, setuptools
, fabric
, typing-extensions
, linien-common
}:

buildPythonPackage {
  pname = "linien-client";
  inherit version;
  pyproject = true;

  inherit src;

  nativeBuildInputs = [
    setuptools
  ];

  propagatedBuildInputs = [
    fabric
    typing-extensions
    linien-common
  ];

  # Same issue as explained in ../linien-common/pkg.nix
  preBuild = ''
    export HOME="$(mktemp -d)"
  '';

  pythonImportsCheck = [
    "linien_client"
  ];

  meta = with lib; {
    description = "Client components of the Linien spectroscopy lock application";
    homepage = "https://github.com/linien-org/linien";
    license = licenses.gpl3;
  };
}
