from PySide6.QtSql import QSqlTableModel


class TableModel:
    def get_table_model(self):
        model = QSqlTableModel()
        model.setTable("table_one")
        model.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        model.select()
        return model
