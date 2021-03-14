import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from models.database import Database
from gui.mainwindow import Ui_DressShopWindow

class DressShop(QMainWindow):

    def __init__(self, data: Database, parent=None):
        super(DressShop, self).__init__(parent)
        self.ui = Ui_DressShopWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    data = Database('storage.db')

    app = QApplication(sys.argv)
    shop = DressShop(data)
    shop.show()
    sys.exit(app.exec_())
