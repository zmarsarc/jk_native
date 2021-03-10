from PySide6.QtWidgets import *
from PySide6.QtCore import *
from models.jk_model import JKModel


class JKEditController(QStyledItemDelegate):

    def __init__(self, parent=None):
        super(JKEditController, self).__init__(parent)

    def createEditor(self, parent, option: QStyleOptionViewItem, index: QModelIndex) -> QWidget:
        if index.column() == JKModel.JK_NAME:
            return JKNameEditor.create_editor(parent)
        if index.column() == JKModel.JK_SIZE_CODE:
            return JKSizeEditor.create_editor(parent, index.model())
        if index.column() == JKModel.JK_LENGTH:
            return JKLengthEditor.create_editor(parent)
        if index.column() == JKModel.JK_COUNT:
            return JKCountEditor.create_editor(parent)
        raise NotImplementedError()

    def setEditorData(self, editor: QWidget, index: QModelIndex):
        if index.column() == JKModel.JK_NAME:
            return JKNameEditor.update_editor_data(editor, index)
        if index.column() == JKModel.JK_SIZE_CODE:
            return JKSizeEditor.update_editor_data(editor, index)
        if index.column() == JKModel.JK_LENGTH:
            return JKLengthEditor.update_editor_data(editor, index)
        if index.column() == JKModel.JK_COUNT:
            return JKCountEditor.update_editor_data(editor, index)
        raise NotImplementedError()

    def setModelData(self, editor: QWidget, model: JKModel, index: QModelIndex):
        if index.column() == JKModel.JK_NAME:
            return JKNameEditor.set_jk_name(editor, model, index)
        if index.column() == JKModel.JK_SIZE_CODE:
            return JKSizeEditor.set_jk_size(editor, model, index)
        if index.column() == JKModel.JK_LENGTH:
            return JKLengthEditor.set_jk_length(editor, model, index)
        if index.column() == JKModel.JK_COUNT:
            return JKCountEditor.set_jk_count(editor, model, index)
        raise NotImplementedError()

    def updateEditorGeometry(self, editor: QComboBox, option: QStyleOptionViewItem, index):
        editor.setGeometry(option.rect)


class JKNameEditor:

    @staticmethod
    def create_editor(parent):
        return QLineEdit('', parent)

    @staticmethod
    def set_jk_name(editor: QLineEdit, model: JKModel, index: QModelIndex):
        name = editor.text()
        if name not in model.names:
            return model.setData(index, name, Qt.EditRole)

        # 名称重复给一个告警
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(f'名称"{name}"已经使用过了')
        msg.exec_()

    @staticmethod
    def update_editor_data(editor: QLineEdit, index: QModelIndex):
        name = str(index.model().data(index, Qt.EditRole))
        editor.setText(name)


class JKSizeEditor:

    @staticmethod
    def create_editor(parent: QWidget, model: JKModel) -> QWidget:
        selector = QComboBox(parent)
        available_size = QStringListModel(list(dict.fromkeys([x.size_code.upper() for x in model.sizes])))
        selector.setModel(available_size)
        selector.setCurrentIndex(0)
        return selector

    @staticmethod
    def update_editor_data(editor: QComboBox, index: QModelIndex):
        val = index.model().data(index, Qt.EditRole)
        editor.setCurrentText(val.size.size_code.upper())

    @staticmethod
    def set_jk_size(editor: QComboBox, model: JKModel, index: QModelIndex):
        current_size = editor.currentText()
        model.setData(index, current_size, Qt.EditRole)


class JKLengthEditor:

    @staticmethod
    def create_editor(parent: QWidget) -> QWidget:
        selector = QSpinBox(parent)
        selector.setMinimum(0)
        selector.setValue(42)
        return selector

    @staticmethod
    def update_editor_data(editor: QSpinBox, index: QModelIndex):
        val = index.model().data(index, Qt.EditRole)
        editor.setValue(val.size.length)

    @staticmethod
    def set_jk_length(editor: QSpinBox, model: JKModel, index: QModelIndex):
        length = editor.value()
        model.setData(index, length, Qt.EditRole)


class JKCountEditor:

    @staticmethod
    def create_editor(parent: QWidget) -> QWidget:
        counter = QSpinBox(parent)
        counter.setMinimum(0)
        counter.setValue(0)
        return counter

    @staticmethod
    def update_editor_data(editor: QSpinBox, index: QModelIndex):
        val = index.model().data(index, Qt.EditRole)
        editor.setValue(val.count)

    @staticmethod
    def set_jk_count(editor: QSpinBox, model: JKModel, index: QModelIndex):
        model.setData(index, editor.value(), Qt.EditRole)