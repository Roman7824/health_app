from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
class Test(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

        self.result = QLabel(txt_workheart + self.result())
        self.index = QLabel(txt_index + str(self.index))

        self.r_line.addWidget(self.result, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.index, alignment = Qt.AlignCenter)
    
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        pass
    def result(self):
        self.index = (4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if self.exp.age >= 7 and self.exp.age<9:
            if self.index >=21:
                return txt_res1
        elif self.index>=17 and self.index<=21:
            return txt_res2
        elif self.index>=12 and self.inde<=17:
            return txt_res3
        elif self.index>=6.5 and self.index<=12:
            return txt_res4
        elif self.index<=6.4:
            return txt_res5
        
        if self.exp.age >= 9 and self.exp.age<=10:
            if self.index >=19.5:
                return txt_res1
        elif self.index>=15.5 and self.index<=19.4:
            return txt_res2
        elif self.index>=10.5 and self.inde<=15.4:
            return txt_res3
        elif self.index>=5 and self.index<=10.4:
            return txt_res4
        elif self.index<=4.9:
            return txt_res5

        if self.exp.age >= 11 and self.exp.age<=12:
            if self.index >18:
                return txt_res1
        elif self.index>=14 and self.index<=17.9:
            return txt_res2
        elif self.index>=9 and self.inde<=13.9:
            return txt_res3
        elif self.index>=3.5 and self.index<=8.9:
            return txt_res4
        elif self.index<=3.4:
            return txt_res5
        
        if self.exp.age >=13 and self.exp.age<14:
            if self.index >=16.5:
                return txt_res1
        elif self.index>=12.5 and self.index<=16.4:
            return txt_res2
        elif self.index>=7.5 and self.inde<=12.4:
            return txt_res3
        elif self.index>=2 and self.index<=7.4:
            return txt_res4
        elif self.index<=1.9:
            return txt_res5
        
        if self.exp.age >= 15:
            if self.index >15:
                return txt_res1
        elif self.index>=11 and self.index<=14.9:
            return txt_res2
        elif self.index>=6 and self.inde<=10.9:
            return txt_res3
        elif self.index>=0.5 and self.index<=5.9:
            return txt_res4
        elif self.index<=0.4:
            return txt_res5
