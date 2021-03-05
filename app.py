import sys
from PySide6 import QtWidgets
from models.database import Database
from models.jk_model import JKModel

SIZE_XS = 30
SIZE_S = 31
SIZE_M = 32
SIZE_L = 33
SIZE_XL = 34


if __name__ == '__main__':
    db = Database('storage.db')

    app = QtWidgets.QApplication([])

    model = JKModel(db)
    view = QtWidgets.QTableView()
    view.setModel(model)

    button = QtWidgets.QPushButton('add new')
    button.clicked.connect(lambda: model.insertRows(0, 1, model.index(0, 0)))

    splitter = QtWidgets.QSplitter()
    splitter.addWidget(view)
    splitter.addWidget(button)

    splitter.setMinimumSize(800, 600)
    splitter.show()

    sys.exit(app.exec_())
