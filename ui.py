# ui.py

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout, QLineEdit, QComboBox) # type: ignore
from PyQt5.QtGui import QIcon # type: ignore
from PyQt5 import QtCore # type: ignore

class View(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.le1=QLineEdit('0',self)
        self.le1.setAlignment(QtCore.Qt.AlignRight)

        self.le2=QLineEdit('0',self)
        self.le2.setAlignment(QtCore.Qt.AlignRight)

        self.cb = QComboBox(self)
        self.cb.addItem(['+', '-', '*', '/'])

        self.formular = QHBoxLayout()
        self.formular.addWidget(self.le1)
        self.formular.addWidget(self.cb)
        self.formular.addWidget(self.le2)
        
        self.btn1 = QPushButton('Message', self)
        # self.btn1.clicked.connect(self.activateMessage)

        self.btn2 = QPushButton('Clear', self)
        # self.btn2.clicked.connect(self.clearMessage)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(self.formular)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256, 256)
        self.show()

    def activateMessage(self):
        self.te1.appendPlainText('Button clicked!')

    def clearMessage(self):
        self.te1.clear()
