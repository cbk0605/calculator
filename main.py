# This code is a simple calculator GUI using PyQt5.
# It creates a window with the title "Calculator" and a size of 256x256 pixels.

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox) # type: ignore # QMessageBox : 메세지박스 위젯
from PyQt5.QtGui import QIcon  # type: ignore # Qicon : 아이콘을 표시하기 위한 클래스
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initGui()

    def initGui(self):
        self.btn1=QPushButton('Message',self) # QPushButton : 버튼 위젯을 생성하는 클래스
        self.btn1.clicked.connect(self.activateMessage) # 버튼 클릭 시 activateMessage 메서드 호출

        vbox=QVBoxLayout()
        vbox.addWidget(self.btn1) # QVBoxLayout : 수직 레이아웃을 생성하는 클래스
        vbox.addStretch(1)  # addStretch : 레이아웃에 여백을 추가하는 메서드
        vbox.addWidget(self.btn1)   # 버튼을 레이아웃에 추가
        vbox.addStretch(1)  # addStretch : 레이아웃에 여백을 추가하는 메서드

        self.setLayout(vbox)    # 레이아웃 설정

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))   # 윈도우 아이콘 설정
        self.resize(256,256)
        self.show()

    def activateMessage(self):  # 메세지 박스를 생성하는 메서드
        QMessageBox.information(self, 'information', 'Button clicked!') # QMessageBox : 메세지박스 위젯을 생성하는 클래스
        # information : 정보 메세지 박스를 생성하는 메서드  

if __name__ == '__main__':  #   This is the main entry point of the program.
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())

# This code creates a simple GUI window for a calculator using PyQt5.
# The window has a title "Calculator" and a size of 256x256 pixels. 
