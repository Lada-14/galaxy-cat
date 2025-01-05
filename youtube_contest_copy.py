from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton

app = QApplication([])
main_window = QWidget() #создание приложения и главного окна
main_window.show()
main_window.resize(500,400)
main_window.setWindowTitle('Покупка "Игры"')#создание виджетов главного окна
q = QLabel('Возраст:') 
a = QRadioButton('меньше 6')
b = QRadioButton('6 и больше')

line_1 = QHBoxLayout()

line_1.addWidget(q, alignment = Qt.AlignCenter)
line_1.addWidget(a, alignment = Qt.AlignCenter)
line_1.addWidget(b, alignment = Qt.AlignCenter)

main_window.setLayout(line_1)

def victory():
    game = QMessageBox()
    game.setText('Покупка произошла успешно!')
    game.exec_()

def not_game():
    game = QMessageBox()
    game.setText('Покупка не произошла.')
    game.exec_()

a.clicked.connect(not_game)
b.clicked.connect(victory)

app.exec_()

#возраст 6+
#деньги 300 руб
