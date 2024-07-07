from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
main_win = QWidget()

main_win.resize(400, 400)

main_win.setWindowTitle('Визначник переможця')
button = QPushButton('Згенерувати')
text = QLabel('Натисни, щоб дізнатися переможця')
winner = QLabel('?')

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(line)

def show_winner():
    num = randint(0, 99)
    winner.setText(str(num))
    text.setText("Переможець:")

button.clicked.connect(show_winner)

main_win.show()
app.exec_()














































































