# This code is a simple calculator GUI using PyQt5.
# It creates a window with the title "Calculator" and a size of 256x256 pixels.

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QPlainTextEdit, QHBoxLayout) # type: ignore # QMessageBox : 메세지박스 위젯 생성하는 클래스
# QHBoxLayout : 수평 레이아웃을 생성하는 클래스 추가

from PyQt5.QtGui import QIcon  # type: ignore # Qicon : 아이콘을 표시하기 위한 클래스
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initGui()

    def initGui(self):
        self.te1=QPlainTextEdit()   # QPlainTextEdit : 여러 줄의 텍스트를 표시하는 위젯
        self.te1.setReadOnly(True)  # 텍스트 편집 불가 설정

        self.btn1=QPushButton('Message',self) # QPushButton : 버튼 위젯을 생성하는 클래스
        self.btn1.clicked.connect(self.activateMessage) # 버튼 클릭 시 activateMessage 메서드 호출

        self.btn2=QPushButton('Clear',self) # QPushButton : 버튼 위젯을 생성하는 클래스
        self.btn2.clicked.connect(self.clearMessage) # 버튼 클릭 시 activateMessage 메서드 호출
        
        hbox=QHBoxLayout()  # QHBoxLayout : 수평 레이아웃을 생성하는 클래스
        hbox.addStretch(1) # 공간을 추가하는 메서드
        hbox.addWidget(self.btn1)   # 버튼1 위젯 추가
        hbox.addWidget(self.btn2)   # 버튼2 위젯 추가

        vbox=QVBoxLayout()
        # vbox.addStretch(1)  # addStretch : 레이아웃에 여백을 추가하는 메서드
        vbox.addWidget(self.te1)    # 수직 레이아웃에 텍스트 에디트 위젯 추가
        # vbox.addWidget(self.btn1) # QVBoxLayout : 수직 레이아웃을 생성하는 클래스
        vbox.addLayout(hbox)  # btn1위치에 hbox 레이아웃 추가
        vbox.addStretch(1)  # addStretch : 레이아웃에 여백을 추가하는 메서드

        self.setLayout(vbox)    # 레이아웃 설정

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))   # 윈도우 아이콘 설정
        self.resize(256,256)
        self.show()

    def activateMessage(self):  # 핸들러 함수 수정 : 메세지가 텍스트 에디트에 출력되도록
        # QMessageBox.information(self, 'information', 'Button clicked!') # QMessageBox : 메세지박스 위젯을 생성하는 클래스
        self.te1.appendPlainText('Button clicked!')
        # information : 정보 메세지 박스를 생성하는 메서드  

    def clearMessage(self):  # 핸들러 함수 수정 : 메세지가 텍스트 에디트에 출력되도록
        self.te1.clear()
        
if __name__ == '__main__':  #   This is the main entry point of the program.
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())

# This code creates a simple GUI window for a calculator using PyQt5.
# The window has a title "Calculator" and a size of 256x256 pixels. 
