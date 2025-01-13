import sys
import typing as tp

import edifice as ed
from PySide6 import QtWidgets
from edifice import Window, component, use_state

from data.db_connection import create_connection
from ui.features.main_window.main_window import MainWindow


@component
def MyApp(self):
    def initializer():
        if not create_connection():
            sys.exit(-1)

        qapp = tp.cast(QtWidgets.QApplication, QtWidgets.QApplication.instance())
        qapp.setApplicationName("Python GUI test")
        if ed.theme_is_light():
            qapp.setPalette(ed.palette_edifice_light())
        else:
            qapp.setPalette(ed.palette_edifice_dark())

    _, _ = use_state(initializer)

    with Window(title="Python GUI test", _size_open=(520, 350)):
        MainWindow()
