import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import sqlite3

SIZE_XS = 30
SIZE_S = 31
SIZE_M = 32
SIZE_L = 33
SIZE_XL = 34

def size_code_to_str(code: int) -> str:
    pass

def size_str_to_code(size: str) -> int:
    pass


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.hello = ['hello welt', 'Hei maailma', 'Hola Mundo', 'ni hao']
        
        self.button = QtWidgets.QPushButton('Click me!')

        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["名字", "尺码", "群长", "库存"])

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)


    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

    def add_item(self, name, size, length, count):
        row = self.table.rowCount()
        self.table.setRowCount(row + 1)
        self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(name))
        self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(size)))
        self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(length)))
        self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(count)))

if __name__ == '__main__':
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS jk(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, size SMALLINT NOT NULL, length INT NOT NULL DEFAULT(0), count INT NOT NULL DEFAULT(0));')
    conn.commit()

    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    for row in c.execute('SELECT name, size, length, count FROM jk'):
        widget.add_item(row[0], row[1], row[2], row[3])

    sys.exit(app.exec_())
    conn.close()
