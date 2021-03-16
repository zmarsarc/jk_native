import sys
from PySide6.QtWidgets import QApplication
from views import DressShopMainWindow
from data.sqlite import SQLiteDriver
import data

if __name__ == '__main__':
    data_driver = SQLiteDriver('storage.db')
    goods_data = data.Goods(data_driver)

    app = QApplication(sys.argv)
    shop = DressShopMainWindow(goods_data)
    shop.show()
    sys.exit(app.exec_())
