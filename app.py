import sys
from PySide6 import QtWidgets
from models.database import Database
from models.jk_model import JKModel
from controllers.jk_edit_controller import JKSizeEditController


if __name__ == '__main__':
    db = Database('storage.db')

    app = QtWidgets.QApplication([])

    model = JKModel(db)
    view = QtWidgets.QTableView()
    view.setModel(model)
    view.setItemDelegateForColumn(1, JKSizeEditController())

    button = QtWidgets.QPushButton('add new')
    button.clicked.connect(model.create_new_jk)

    splitter = QtWidgets.QSplitter()
    splitter.addWidget(view)
    splitter.addWidget(button)

    splitter.setMinimumSize(800, 600)
    splitter.show()

    sys.exit(app.exec_())
