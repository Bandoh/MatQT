import sys
import random
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton,QWidget, QVBoxLayout
from PyQt6.QtGui import QPixmap
sys.path.insert(0,"C:/Users/Kelvin/Documents/PortableGit/projects/python/MatQT/MaterialQT")
from MColors import MatColors
from MButton import MButton
# from PyQt6.QtCore import Qt


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Tral")
window.setStyleSheet("background-color: {}".format(MatColors['white']))


v = QVBoxLayout(window)
btn = MButton("E", window)

v.addWidget(btn)

window.show()
sys.exit(app.exec())