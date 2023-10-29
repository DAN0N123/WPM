from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QVBoxLayout, QWidget
import random
import time
import sys

subjects = ["cat", "dog", "friend", "sun", "bird", "car", "mailman", "buddy", "entrepreneur"]
verbs = ["jumps", "runs", "sings", "sleeps", "eats", "delivered", "bought", "told"]
adjectives = ["A quick", "The lazy", "The happy", "A bright", "The friendly", "A witty", "An instinctive", "His own"]
objects = ["the ball", "a book", "the sky", "a rainbow", "a sandwich", "an apple", "the program"]


text = ""

word_count = 0
while word_count < 70:
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)
    object_ = random.choice(objects)
    sentence = f"{adjective} {subject} {verb} {object_}. "
    
    sentence_word_count = len(sentence.split())
    if word_count + sentence_word_count <= 70:
        text += sentence
        word_count += sentence_word_count
    else:
        break



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 950, 753)
        self.setWindowTitle("WPM")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 30, 390, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText('WPM CALCULATOR')

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 850, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setText(text)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(190, 290, 571, 231))
        self.textEdit.setObjectName("textEdit")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(820, 30, 118, 23))
        self.progressBar.setMaximum(60)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")

        self.setCentralWidget(self.centralwidget)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.start_timer()
        
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
            self.timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec_())


