from PySide6.QtWidgets import QTableView


class InventoryView(QTableView):

    def __init__(self, parent=None):
        super(InventoryView, self).__init__(parent)