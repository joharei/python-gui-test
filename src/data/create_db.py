from PySide6 import QtWidgets
from PySide6.QtSql import QSqlDatabase, QSqlQuery


def create_db():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('../test.db')

    # try to open the database
    if not db.open():
        raise Exception("Could not open the database")

    query = QSqlQuery()

    # create a table
    query.exec('''create table table_one(
    id INTEGER PRIMARY KEY, fruit TEXT, inventory int);''')

    # populate the table
    query.exec("insert into table_one (fruit, inventory) values('banana', 3);")
    query.exec("insert into table_one (fruit, inventory) values('mango', 10);")
    query.exec("insert into table_one (fruit, inventory) values('cherry', 55);")

    db.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    create_db()
