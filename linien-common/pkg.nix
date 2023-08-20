{ lib
, buildPythonPackage
, version
, src
, setuptools
, numpy
, scipy
, importlib-metadata
, rpyc
, appdirs
}:

buildPythonPackage {
  pname = "linien-common";
  inherit version;
  pyproject = true;

  inherit src;

  nativeBuildInputs = [
    setuptools
  ];

  propagatedBuildInputs = [
    numpy
    scipy
    importlib-metadata
    rpyc
    appdirs
  ];

  # Even simply importing linien_common, requires having a valid home
  # directory. Using preCheck is not early enough since the pythonImportsCheck
  # phase is being run before.
  preBuild = ''
    export HOME="$(mktemp -d)"
  '';

  pythonImportsCheck = [
    "linien_common"
  ];

  meta = with lib; {
    description = "Shared components of the Linien spectroscopy lock application";
    homepage = "https://github.com/linien-org/linien";
    license = licenses.gpl3;
  };
}
