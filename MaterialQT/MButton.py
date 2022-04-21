import sys
from PyQt6.QtWidgets import QPushButton
from MColors import MatColors



class MButton(QPushButton):
    color = MatColors['black']

    def __init__(self,a):
        super().__init__(self)
        print(a)
        # super().setStyleSheet("background-color: {}".format(color))
        pass




    