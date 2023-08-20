{ lib
, buildPythonPackage
, version
, src
, setuptools
, requests
, pyqtgraph
, pyqt5
, superqt
, click
, linien-client
, qt5
, makeDesktopItem
, copyDesktopItems
, graphicsmagick
}:

buildPythonPackage rec {
  pname = "linien-gui";
  inherit version;
  pyproject = true;

  inherit src;

  nativeBuildInputs = [
    setuptools
    qt5.wrapQtAppsHook
    copyDesktopItems
    graphicsmagick
  ];

  buildInputs = [
    qt5.qtbase
    qt5.qtwayland
  ];

  propagatedBuildInputs = [
    requests
    pyqtgraph
    pyqt5
    superqt
    click
    linien-client
  ];

  dontWrapQtApps = true;
  preFixup = ''
    makeWrapperArgs+=("''${qtWrapperArgs[@]}")
  '';
  desktopItems = makeDesktopItem {
    name = meta.mainProgram;
    exec = meta.mainProgram;
    icon = meta.mainProgram;
    desktopName = meta.mainProgram;
    comment = meta.description;
    type = "Application";
    categories = [ "Science" ];
  };

  postInstall = ''
    mkdir -p $out/share/icons/hicolor/256x256/apps/
    gm convert linien_gui/icon.ico $out/share/icons/hicolor/256x256/apps/${meta.mainProgram}.png
  '';

  # Same issue as explained in ../linien-common/pkg.nix
  preBuild = ''
    export HOME="$(mktemp -d)"
  '';

  pythonImportsCheck = [
    "linien_gui"
  ];

  meta = with lib; {
    description = "Graphical user interface of the Linien spectroscopy lock application";
    homepage = "https://github.com/linien-org/linien";
    license = licenses.gpl3;
    mainProgram = "linien";
  };
}
