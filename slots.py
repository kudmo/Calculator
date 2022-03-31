"""
Пользовательские слоты для виджетов.
"""
# Импортируем модуль времени
from datetime import datetime
# Импортируем класс интерфейса из созданного конвертером модуля 
from form_ui import Ui_Form


# Создаём собственный класс, наследуясь от автоматически сгенерированного
class MainWindowSlots(Ui_Form):
    
    # Определяем пользовательский слот
    def number_e_clicked(self):
        self.Input_order.setText(self.Input_order.text()+" e ")
        return None
    def number_pi_clicked(self):
        self.Input_order.setText(self.Input_order.text()+" pi ")
        return None
    def number_0_clicked(self):
        self.Input_order.setText(self.Input_order.text()+"0")
        return None
    def number_1_clicked(self):
        self.Input_order.setText(self.Input_order.text()+"1")
        return None
    def number_2_clicked(self):
        self.Input_order.setText(self.Input_order.text()+"2")
        return None
    def number_3_clicked(self):
        self.Input_order.setText(self.Input_order.text()+"3")
        return None
    def number_4_clicked(self):
        self.Input_order.setText(self.Input_order.text()+"4")
        return None
    def number_5_clicked(self):
        self.Input_order.setText(self.Input_order.text()+"5")
        return None
    def number_6_clicked(self):
        self.Input_order.setText(self.Input_order.text()+"6")
        return None    
    def number_7_clicked(self):
        self.Input_order.setText(self.Input_order.text()+"7")
        return None
    def number_8_clicked(self):
        self.Input_order.setText(self.Input_order.text()+"8")
        return None
    def number_9_clicked(self):
        self.Input_order.setText(self.Input_order.text()+"9")
        return None
    
    