from PySide6 import QtWidgets
from PySide6.QtCore import QAbstractItemModel
from edifice import CustomWidget


class TableView(CustomWidget):
	def __init__(
			self,
			model: QAbstractItemModel,
			hide_columns: list[int] = None,
	):
		super().__init__()
		if hide_columns is None:
			hide_columns = []
		self._register_props(
			{
				"model": model,
				"hide_columns": hide_columns,
			}
		)

	def create_widget(self):
		return QtWidgets.QTableView()

	def paint(self, widget: QtWidgets.QTableView, newprops):
		for prop in newprops:
			if prop == "model":
				widget.setModel(newprops[prop])
			if prop == "hide_columns":
				for column in newprops[prop]:
					widget.hideColumn(column)
