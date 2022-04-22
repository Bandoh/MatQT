import sys
import random
import pathlib
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton,QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap



materialPath = str(pathlib.Path(__file__).parent.resolve())+"/MaterialQT".replace("\\","/")
sys.path.insert(0,materialPath)
from MColors import MatColors
from MButton import MButton
# from PyQt6.QtCore import Qt


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Music Me")
window.setFixedWidth(1024)
window.setFixedHeight(600)
window.setStyleSheet("background-color: {}".format(MatColors['white']))
window.move(100,100)


v = QHBoxLayout(window)
btn = MButton("Click ME", window)
btn1 = MButton("Click ME", window)

v.addWidget(btn)
v.addWidget(btn1)
v.addWidget(btn)

window.show()
sys.exit(app.exec())