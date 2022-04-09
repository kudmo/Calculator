from PyQt5.QtWidgets import QWidget,QGroupBox,QFormLayout, QVBoxLayout, QScrollArea,QLabel
from PyQt5 import QtCore
#from slots import HistoryWindowSlots

class HistoryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.group_box = QGroupBox()
        self.form_layout = QFormLayout()
        self.group_box.setLayout(self.form_layout)
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.group_box)
        self.scroll.setWidgetResizable(True)
        self.scroll.setFixedHeight(400)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.scroll)
    
    def addNewOrderInHistory(self,text:str)->None:
        """
        Add a new label in history with a content = text
        """
        self.form_layout.addWidget(QLabel(text))
        QtCore.QTimer.singleShot(100, self.scrollDown)
        return None
    def scrollDown(self)->None:
        """
        Scroll history bar to the end
        """
        last_position = self.scroll.verticalScrollBar().maximum()
        self.scroll.verticalScrollBar().setSliderPosition(last_position)
        return None