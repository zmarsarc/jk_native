from PySide6.QtWidgets import (
    QDialog, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
)

class NewJKDialog(QDialog):
    
    def __init__(self, parent=None):
        super(NewJKDialog, self).__init__(parent)
        self.setWindowTitle("添加新JK")

        self.name_input =QLineEdit()
        self.size_selector = QComboBox()
        self.length_selector = QComboBox()
        self.count_input = QLineEdit()

        self.ok_button = QPushButton("确认")
        self.ok_button.clicked.connect(self.accept)
        self.ok_button.setDefault(True)

        self.abort_button = QPushButton("取消")
        self.abort_button.clicked.connect(self.reject)

        root = QVBoxLayout()

        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("名称"))
        name_layout.addWidget(self.name_input)
        root.addLayout(name_layout)

        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel("尺码"))
        size_layout.addWidget(self.size_selector)
        root.addLayout(size_layout)

        length_layout = QHBoxLayout()
        length_layout.addWidget(QLabel("裙长"))
        length_layout.addWidget(self.length_selector)
        root.addLayout(length_layout)

        count_layout = QHBoxLayout()
        count_layout.addWidget(QLabel("库存"))
        count_layout.addWidget(self.count_input)
        root.addLayout(count_layout)

        button_box = QHBoxLayout()
        button_box.addWidget(self.abort_button)
        button_box.addWidget(self.ok_button)
        root.addLayout(button_box)
       
        self.setLayout(root)

    def jk_information(self):
        return (
            self.name_input.text(), self.size_selector.currentText(),
            self.length_selector.currentText(), self.count_input.text()
        )

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    dialog = NewJKDialog()
    dialog.show()

    sys.exit(app.exec_())