import sys
from PySide6.QtWidgets import QApplication
from views import DressShopMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    shop = DressShopMainWindow()
    shop.show()
    sys.exit(app.exec_())
