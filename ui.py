# ui.py

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout, QLabel) # type: ignore
from PyQt5.QtGui import QIcon # type: ignore
from PyQt5.QtCore import QDate, Qt # type: ignore 

class View(QWidget):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate() # Current date
        self.initUi()

    def initUi(self):
        self.lbl1 = QLabel(self.date.toString(Qt.DefaultLocaleLongDate), self)
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

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
        vbox.addLayout(hbox)
        vbox.addWidget(self.lbl1)
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
