from PySide6.QtSql import QSqlDatabase, QSqlQuery
from edifice import alert


def create_connection():
	db = QSqlDatabase.addDatabase("QSQLITE")
	db.setDatabaseName("test.db")
	if not db.open():
		alert("Could not open the database", ["Ok"])
		return False

	return True
