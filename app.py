import sys
import random
from PySide6 import QtCore, QtWidgets
from models.database import Database
from models.jk_model import JKModel

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
    db = Database('storage.db')

    app = QtWidgets.QApplication([])

    model = JKModel(db)
    view = QtWidgets.QTableView()
    view.setModel(model)
    view.show()

    sys.exit(app.exec_())
