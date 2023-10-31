from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QVBoxLayout, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QKeyEvent
import random
import time
import sys
from word_generator import get_word


text = get_word()

class Window(QtWidgets.QMainWindow):
    global text
    

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 950, 750)
        self.setWindowTitle("WPM")

        self.score = None
        self.game_started = False
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.font_start = QtGui.QFont()
        self.font_start.setPointSize(25)
        self.font_start.setBold(True)
        self.font_start.setWeight(75)

        self.font_gen = QtGui.QFont()
        self.font_gen.setPointSize(15)
        self.font_gen.setBold(True)
        self.font_gen.setWeight(75)

        
        self.initial_label=QtWidgets.QLabel(self.centralwidget)
        self.initial_label.setGeometry(QtCore.QRect(235,250, 480, 100))
        self.initial_label.setFont(self.font_start)
        self.initial_label.setObjectName("initial_label")
        self.initial_label.setWordWrap(True)
        self.initial_label.setText('PRESS ANYTHING TO START')

        self.countdown_label = QtWidgets.QLabel(self.centralwidget)
        self.countdown_label.setGeometry(QtCore.QRect(460,330, 30, 30))
        self.countdown_label.setFont(self.font_start)
        self.countdown_label.setText('')

        self.setCentralWidget(self.centralwidget)

    def game_screen(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label=QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(315,30,320,41))
        self.label.setFont(self.font_start)
        self.label.setObjectName("label")
        self.label.setText('WPM CALCULATOR')

        self.label_2=QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40,100,850,131))
        self.label_2.setFont(self.font_gen)
        self.label_2.setText(text)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.textEdit=QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(190,290,571,231))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(self.get_text)

        self.progressBar=QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(820,30,118,23))
        self.progressBar.setMaximum(60)
        self.progressBar.setProperty("value",0)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")

        self.setCentralWidget(self.centralwidget)

        self.timer=QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.start_timer()
        

    def keyPressEvent(self, event):
        if event.key() and not self.game_started:
            self.start_game()
    
    def start_game(self):
        self.game_started =  True
        self.initial_label.hide()
        self.countdown_value = 3
        self.countdown_label.setText(str(self.countdown_value))
        self.timerx = QTimer(self)
        self.timerx.timeout.connect(self.update_countdown)
        self.timerx.start(1000)  

    def update_countdown(self):
        self.countdown_value -= 1
        if self.countdown_value > 0:
            self.countdown_label.setText(str(self.countdown_value))
        else:
            QtCore.QTimer.singleShot(50, self.countdown_label.hide)
            self.timerx.stop()
            QtCore.QTimer.singleShot(100, self.game_screen)

    def check_win(self):
        textx = self.textEdit.toPlainText()
        if textx + ' ' == text: 
            time = self.progressBar.value() / 60
            yo = text.split(' ')
            self.score = (f"{len(yo) / time} WPM")
            self.timer.stop()
            self.end_screen()
            
        

    def start_timer(self):
            self.start_time = time.time()
            self.timer_duration = 60
            self.timer.start(1000)

    def update_timer(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time

        if elapsed_time <= self.timer_duration:
            self.progressBar.setValue(int(elapsed_time))
        else:
            self.progressBar.setValue(int(elapsed_time))
            textx = self.textEdit.toPlainText()
            yo = textx.split(' ')
            self.score = (f"{len(yo)} WPM")
            self.timer.stop()
            self.end_screen()
    def get_text(self):
        global text
        self.check_win()
        textx = self.textEdit.toPlainText() 
        texty = ''
        for index, char in enumerate(textx):
            if char != text[index]:
                texty += f"<font color='red'>{text[index]}</font>"

                labeltext = f"{texty}{text[index + 1:]}"
            if char == text[index]:
                texty += f"<font color='green'>{text[index]}</font>"
                labeltext = f"{texty}{text[index + 1:]}"
            if len(text) == 0:
                labeltext = text

            self.label_2.setText(labeltext)
    def end_screen(self):
        self.game_started = False
        self.label_2.hide()
        self.progressBar.hide()
        self.textEdit.hide()
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.score_showcase = QtWidgets.QLabel(self.centralwidget)
        self.score_showcase.setGeometry(QtCore.QRect(365,300,220,70)) 
        self.score_showcase.setStyleSheet("QLabel { border: 2px solid black; padding: 10px; }")
        self.score_showcase.setFont(self.font_start)
        self.score_showcase.setText(self.score)
        self.setCentralWidget(self.centralwidget)    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Window()
    

    main_window.show()
    sys.exit(app.exec_())


