from PySide6.QtCore import Qt
from edifice import use_state

from ui.features.table.table_model import TableModel


def use_table_view_model():
    view_model, _ = use_state(TableModel())

    def get_table_model():
        model = view_model.get_table_model()
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Fruit")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Inventory")
        return model

    return get_table_model
