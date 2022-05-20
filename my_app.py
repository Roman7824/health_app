from instr import *
from second_win import *
from final_win import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.hello_txt = QLabel(txt_hello)
        self.line = QVBoxLayout()
        self.line.addWidget(self.hello_txt, alignment = Qt.AlignLeft)
        self.line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.line.addWidget(self.button, alignment = Qt.AlignCenter)
        self.setLayout(self.line)
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = Testwin()
App = QApplication([1000, 600])
main_win = MainWin()
App.exec_()