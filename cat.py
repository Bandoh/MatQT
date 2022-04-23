import sys
import random
import pathlib
from PyQt6.QtWidgets import QApplication, QLabel,QWidget, QHBoxLayout, QLabel,QVBoxLayout, QFrame, QPushButton
from PyQt6 import QtCore



materialPath = str(pathlib.Path(__file__).parent.resolve())+"/MaterialQT".replace("\\","/")
sys.path.insert(0,materialPath)
from MColors import MatColors
from MButton import MButton
# from PyQt6.QtCore import Qt


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Music Me")
# window.setFixedWidth(1224)
# window.setFixedHeight(600)
window.setStyleSheet("background-color: {}".format(MatColors['red']))
window.move(100,100)
# window.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

# btn = MButton("Click ME", window)
# btn1 = MButton("Click ME", window)

primary_color = MatColors['red']
sec_color = MatColors["Dblue"]
background_color = MatColors['white']
background_color1 = MatColors['Dgrey']






vertical_l = QVBoxLayout(window)
horizintal_l  = QHBoxLayout()

vertical_l.setSpacing(0)
horizintal_l.setSpacing(0)
vertical_l.setContentsMargins(0,0,0,0)




left_section = QFrame()
left_section.setStyleSheet("background-color:{}; border-bottom-left-radius:40px;".format(background_color))
left_section.setFixedWidth(200)


vertical_left_layout  = QVBoxLayout(left_section)

vertical_left_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)


lib_label = QLabel("LIBRARY")
lib_label.setContentsMargins(20,0,0,0)
home_btn = MButton("Home",background_color,background_color1)
playlist_btn = MButton("Playlist",background_color,background_color1)
library_btn = MButton("Library",background_color,background_color1)

vertical_left_layout.setContentsMargins(2,50,10,0)
vertical_left_layout.addWidget(lib_label)
vertical_left_layout.addWidget(home_btn)
vertical_left_layout.addWidget(playlist_btn)
vertical_left_layout.addWidget(library_btn)

vertical_left_layout.setSpacing(5)



mid_section = QFrame()
mid_section.setStyleSheet("background-color:{};".format(background_color))
right_section = QFrame()
right_section.setStyleSheet("border-bottom-right-radius:40px;background-color:{};".format(background_color))
right_section.setFixedWidth(200)

horizintal_l.addWidget(left_section)
horizintal_l.addWidget(mid_section)
horizintal_l.addWidget(right_section)


top_section = QLabel()
top_section.setStyleSheet("background-color:{};".format(MatColors['grey']))



down_section = QLabel()
down_section.setStyleSheet("background-color:{};".format(primary_color))
down_section.setFixedHeight(80)

vertical_l.addLayout(horizintal_l)

vertical_l.addWidget(down_section)



window.show()
sys.exit(app.exec())