import sys
from PyQt6.QtWidgets import QPushButton
from MColors import MatColors



class MButton(QPushButton):
    def __init__(a,window,self):
        super().__init__(window)
        self.color = MatColors['grey']
        self.border_radius = 0.0
        super().setStyleSheet('''
        background-color: {};
        border: 14px;
        border-radius: 25px;
        padding: 20px 0;
        *:hover
        '''.format(self.color,"25px"))
        pass




    