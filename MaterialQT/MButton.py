import sys
from PyQt6.QtWidgets import QPushButton
from MColors import MatColors



class MButton(QPushButton):
    def __init__(self,txt,bcolor,txtcolor):
        super().__init__(text=txt)
        self.bcolor = bcolor
        self.color = txtcolor
        self.border_radius = 0.0
        super().setStyleSheet('''
        background-color: {};
        border: 14px;
        border-radius: {};
        padding: 20px 0;
        color:{};

        '''.format(self.bcolor,"15px",self.color)
        
        )
        pass




    