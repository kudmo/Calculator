"""
Пользовательские слоты для виджетов.
"""
# Импортируем модуль времени
from datetime import datetime
# Импортируем класс интерфейса из созданного конвертером модуля
from PyQt5.QtWidgets import QMessageBox
from form_ui import Ui_Form
from calc_processor import Calculator

# Создаём собственный класс, наследуясь от автоматически сгенерированного
class MainWindowSlots(Ui_Form):
    calc = Calculator()
    history = []
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
    
    def operation_plus_clicked(self):
        self.Input_order.setText(self.Input_order.text()+" + ")
        return None
    def operation_minus_clicked(self):
        self.Input_order.setText(self.Input_order.text()+" - ")
        return None
    def operation_multiply_clicked(self):
        self.Input_order.setText(self.Input_order.text()+" * ")
        return None
    def operation_devide_clicked(self):
        self.Input_order.setText(self.Input_order.text()+" / ")
        return None
    def operation_exp_clicked(self):
        self.Input_order.setText(self.Input_order.text()+" ^ ")
        return None
    
    def abs_braces(self):
        self.Input_order.setText(self.Input_order.text()+"|")
        return None
    def left_brace(self):
        self.Input_order.setText(self.Input_order.text()+"(")
        return None
    def right_brace(self):
        self.Input_order.setText(self.Input_order.text()+")")
        return None
    
    def func_sin_clicked(self):
        self.Input_order.setText(self.Input_order.text()+"sin(")
        return None
    def func_cos_clicked(self):
        self.Input_order.setText(self.Input_order.text()+"cos(")
        return None
    def func_tg_clicked(self):
        self.Input_order.setText(self.Input_order.text()+"tg(")
        return None
    def func_log_clicked(self):
        self.Input_order.setText(self.Input_order.text()+"log(")
        return None

    def clear_input(self):
        self.Input_order.setText("")
        return None
    def del_symbol(self):
        self.Input_order.setText(self.Input_order.text()[:-1])
    def calculate_result(self):
        inp = self.Input_order.text()
        res = self.calc.run(inp)
        if not res is None:
            self.clear_input()
            if len(self.history)==5:
                self.history.append(str(res))
                self.history.pop(0)
                self.History.setText(self.history[0] +'\n'
                                    +self.history[1] +'\n'
                                    +self.history[2] +'\n'
                                    +self.history[3] +'\n'
                                    +self.history[4])
            elif len(self.history)==0:
                self.history.append(str(res))
                self.History.setText(self.history[0])
            else:
                self.history.append(str(res))
                self.History.setText(self.History.text() + '\n' + str(res))
        else:
            msg = QMessageBox()
            msg.setWindowTitle("")
            msg.setText("Input isn't correct")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()