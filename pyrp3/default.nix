{ lib
, src
, version
, buildPythonPackage
, setuptools
, setuptools-scm
, importlib-metadata
, myhdl
, rpyc
, cached-property
, numpy
}:

buildPythonPackage {
  pname = "pyrp3";
  inherit version;
  pyproject = true;

  inherit src;

  nativeBuildInputs = [
    setuptools
    setuptools-scm
  ];

  propagatedBuildInputs = [
    importlib-metadata
    myhdl
    rpyc
    cached-property
    numpy
  ];

  pythonImportsCheck = [
    "pyrp3"
    "pyrp3.board"
  ];

  meta = with lib; {
    description = "Python 3 port of PyRedPitaya library providing access to Red Pitaya registers";
    homepage = "https://github.com/linien-org/pyrp3";
    license = licenses.bsd3;
    platforms = platforms.linux;
  };
}
