# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --include-qt-plugins=sqldrivers

from edifice import App

from ui.app import MyApp

if __name__ == "__main__":
    App(MyApp()).start()
