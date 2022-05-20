from instr import *
from final_win import *
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
class Testwin(QWidget):
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
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

        self.name = QLabel(txt_name)
        self.name1 = QLineEdit(txt_hintname)
        self.age = QLabel(txt_age)
        self.age1 = QLineEdit(txt_hintage)
        self.text = QLabel(txt_test1)
        self.but1 = QPushButton(txt_starttest1)
        self.butt1 = QLineEdit(txt_hinttest1)
        self.text1 = QLabel(txt_test2)
        self.but2 = QPushButton(txt_starttest2)
        self.butt2 = QLabel(txt_test3)
        self.but3 = QPushButton(txt_starttest3)
        self.butt3 = QLineEdit(txt_hinttest2)
        self.butt4 = QLineEdit(txt_hinttest3)
        self.but4 = QPushButton(txt_starttest4)
        self.txt_time = QLabel(txt_time)
        self.txt_time.setFont(QFont('Times', 36, QFont.Bold))

        self.l_line.addWidget(self.name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.name1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.age1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.but1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.butt1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.but2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.butt2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.but3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.butt3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.butt4, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.but4, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.txt_time, alignment = Qt.AlignRight)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.but4.clicked.connect(self.next_click)
        self.but1.clicked.connect(self.timer_test1)
        self.but2.clicked.connect(self.timer_test2)
        self.but3.clicked.connect(self.timer_test3)
    def timer_test1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_time.setText(time.toString('hh:mm:ss'))
        self.txt_time.setFont(QFont('Times', 36, QFont.Bold))
        self.txt_time.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    def timer_test2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_time.setText(time.toString('hh:mm:ss')[6:8])
        self.txt_time.setFont(QFont('Times', 36, QFont.Bold))
        self.txt_time.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    def timer_test3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer3Event(self):
       global time
       time = time.addSecs(-1)
       self.txt_time.setText(time.toString("hh:mm:ss"))
       if int(time.toString("hh:mm:ss")[6:8]) >= 45:
           self.txt_time.setStyleSheet("color: rgb(0,255,0)")
       elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
           self.txt_time.setStyleSheet("color: rgb(0,255,0)")
       else:
           self.txt_time.setStyleSheet("color: rgb(0,0,0)")
       self.txt_time.setFont(QFont("Times", 36, QFont.Bold))
       if time.toString("hh:mm:ss") == "00:00:00":
           self.time.stop()

    
    def next_click(self):
        self.hide()
        self.th = Test()