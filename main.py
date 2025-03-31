# This code is a simple calculator GUI using PyQt5.
# It creates a window with the title "Calculator" and a size of 256x256 pixels.

import sys
from PyQt5.QtWidgets import QApplication, QWidget 
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initGui()

    def initGui(self):
        self.setWindowTitle('Calculator')
        self.resize(256,256)
        self.show()

if __name__ == '__main__':  #   This is the main entry point of the program.
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())

# This code creates a simple GUI window for a calculator using PyQt5.
# The window has a title "Calculator" and a size of 256x256 pixels. 
