import sys
from PySide6.QtWidgets import QApplication
from views import DressShopMainWindow
from data.sqlite import SQLiteDriver

if __name__ == '__main__':
    data_driver = SQLiteDriver('storage.db')

    app = QApplication(sys.argv)
    shop = DressShopMainWindow(data_driver)
    shop.show()
    sys.exit(app.exec_())
