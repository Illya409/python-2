from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox

app =QApplication([])
mw = QWidget()
mw.resize(400, 300)

mw.setWindowTitle("Конкурс від Crazy people")

question = QLabel('В якому році канал отримав "золоту кнопку" від YouTube ')

btn1 = QRadioButton('2005')
btn2 = QRadioButton('2010')
btn3 = QRadioButton('2015')
btn4 = QRadioButton('2020')

main_line = QVBoxLayout()

lineH1 = QHBoxLayout()
lineH2 = QHBoxLayout()
lineH3 = QHBoxLayout()

lineH1.addWidget(question, alignment = Qt.AlignCenter)
lineH2.addWidget(btn1, alignment = Qt.AlignCenter)
lineH2.addWidget(btn2, alignment = Qt.AlignCenter)
lineH3.addWidget(btn3, alignment = Qt.AlignCenter)
lineH3.addWidget(btn4, alignment = Qt.AlignCenter)

main_line.addLayout(lineH1)
main_line.addLayout(lineH2)
main_line.addLayout(lineH3)

mw.setLayout(main_line)

def show_win():
    win = QMessageBox()
    win.setText("Вірно!\nВи виграли гіроскутер")
    win.exec_()

def show_lose():
    win = QMessageBox()
    win.setText("Ні, 2015 року!\nВи виграли фірмовий пакет")
    win.exec_()

btn3.clicked.connect(show_win)
btn1.clicked.connect(show_lose)
btn2.clicked.connect(show_lose)
btn4.clicked.connect(show_lose)

mw.show()
app.exec_()














