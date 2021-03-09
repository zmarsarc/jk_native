from typing import Union
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from models.jk_model import JKModel


class JKSizeEditController(QStyledItemDelegate):

    def __init__(self, parent=None):
        super(JKSizeEditController, self).__init__(parent)

    def createEditor(self, parent, option: QStyleOptionViewItem, index: QModelIndex) -> QWidget:
        """设置编辑器，对尺码只提供有限的选项"""
        if index.column() == JKModel.JK_SIZE_CODE:
            selector = QComboBox(parent)
            selector.setGeometry(option.rect)
            return selector
        editor = QLineEdit('', parent=parent)
        return editor

    def setEditorData(self, editor: Union[QLineEdit, QComboBox], index: QModelIndex):
        val = index.model().data(index, Qt.DisplayRole)

        if isinstance(editor, QLineEdit):
            editor.setText(str(val))
        else:
            editor.setCurrentText(str(val).upper())

    def setModelData(self, editor: Union[QLineEdit, QComboBox], model: JKModel, index: QModelIndex):
        # todo: set jk size code
        if index.column() == JKModel.JK_SIZE_CODE:
            pass

        model.setData(index, editor.text())

    def updateEditorGeometry(self, editor: QComboBox, option: QStyleOptionViewItem, index):
        editor.setGeometry(option.rect)
