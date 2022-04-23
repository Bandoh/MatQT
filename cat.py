import sys
import random
import pathlib
from PyQt6.QtWidgets import QApplication, QLabel,QWidget, QHBoxLayout, QLabel



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

left_section = QLabel(window)
left_section.setStyleSheet("background-color:{};".format(MatColors['grey']))
left_section.setFixedWidth(250)

mid_section = QLabel(window)
mid_section.setStyleSheet("background-color:{};".format(MatColors['white']))

right_section = QLabel(window)
right_section.setStyleSheet("background-color:{};".format(MatColors['white']))


v.addWidget(left_section)
v.addWidget(mid_section)
v.addWidget(right_section)

window.show()
sys.exit(app.exec())