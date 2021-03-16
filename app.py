import sys
from PySide6.QtWidgets import QApplication
from models.database import Database
from views import DressShopMainWindow

if __name__ == '__main__':
    data = Database('storage.db')

    app = QApplication(sys.argv)
    shop = DressShopMainWindow()
    shop.show()
    sys.exit(app.exec_())
