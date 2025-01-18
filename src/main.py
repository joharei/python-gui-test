# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --include-qt-plugins=sqldrivers

import logging

from edifice import App

from ui.app import MyApp

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("logger")

if __name__ == "__main__":
    App(MyApp()).start()
