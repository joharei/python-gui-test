import logging
from PySide6 import QtWidgets
from PySide6.QtCore import QDir, QFile
from PySide6.QtSql import QSqlDatabase, QSqlQuery


def connect_to_database():
    db = QSqlDatabase.addDatabase('QSQLITE')

    write_dir = QDir("")
    if not write_dir.mkpath("."):
        logging.error("Failed to create writable directory")

    # Ensure that we have a writable location on all devices.
    abs_path = write_dir.absolutePath()
    filename = f"{abs_path}/test.db"

    # When using the SQLite driver, open() will create the SQLite
    # database if it doesn't exist.
    db.setDatabaseName(filename)
    if not db.open():
        logging.error("Cannot open database")
        QFile.remove(filename)
        return False

    return create_table()

def create_table():
    if "table_one" in QSqlDatabase.database().tables():
        return True

    query = QSqlQuery()

    # create a table
    if not query.exec('''create table table_one(
    id INTEGER PRIMARY KEY, fruit TEXT, inventory int);'''):
        logging.error("Failed to query database")
        return False

    # populate the table
    query.exec("insert into table_one (fruit, inventory) values('banana', 3);")
    query.exec("insert into table_one (fruit, inventory) values('mango', 10);")
    query.exec("insert into table_one (fruit, inventory) values('cherry', 55);")

    return True


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    connect_to_database()
