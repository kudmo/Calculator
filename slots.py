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
    history = ['','','','','']
    # Определяем пользовательский слот
    def numberEilerClicked(self):
        self.Input_order.setText(self.Input_order.text()+" e ")
        return None
    def numberPiClicked(self):
        self.Input_order.setText(self.Input_order.text()+" pi ")
        return None
    def numberZeroClicked(self):
        self.Input_order.setText(self.Input_order.text()+"0")
        return None
    def numberOneClicked(self):
        self.Input_order.setText(self.Input_order.text()+"1")
        return None
    def numberTwoClicked(self):
        self.Input_order.setText(self.Input_order.text()+"2")
        return None
    def numberThreeClicked(self):
        self.Input_order.setText(self.Input_order.text()+"3")
        return None
    def numberFourClicked(self):
        self.Input_order.setText(self.Input_order.text()+"4")
        return None
    def numberFiveClicked(self):
        self.Input_order.setText(self.Input_order.text()+"5")
        return None
    def numberSixClicked(self):
        self.Input_order.setText(self.Input_order.text()+"6")
        return None    
    def numberSevenClicked(self):
        self.Input_order.setText(self.Input_order.text()+"7")
        return None
    def numberEightClicked(self):
        self.Input_order.setText(self.Input_order.text()+"8")
        return None
    def numberNineClicked(self):
        self.Input_order.setText(self.Input_order.text()+"9")
        return None
    
    def operationPlusClicked(self):
        self.Input_order.setText(self.Input_order.text()+" + ")
        return None
    def operationMinusClicked(self):
        self.Input_order.setText(self.Input_order.text()+" - ")
        return None
    def operationMultiplyClicked(self):
        self.Input_order.setText(self.Input_order.text()+" * ")
        return None
    def operationDevideClicked(self):
        self.Input_order.setText(self.Input_order.text()+" / ")
        return None
    def operationExpClicked(self):
        self.Input_order.setText(self.Input_order.text()+"^")
        return None
    
    def absBraces(self):
        self.Input_order.setText(self.Input_order.text()+"|")
        return None
    def leftBrace(self):
        self.Input_order.setText(self.Input_order.text()+"(")
        return None
    def rightBrace(self):
        self.Input_order.setText(self.Input_order.text()+")")
        return None
    
    def funcSinClicked(self):
        self.Input_order.setText(self.Input_order.text()+"sin(")
        return None
    def funcCosClicked(self):
        self.Input_order.setText(self.Input_order.text()+"cos(")
        return None
    def funcTgClicked(self):
        self.Input_order.setText(self.Input_order.text()+"tg(")
        return None
    def funcLogClicked(self):
        self.Input_order.setText(self.Input_order.text()+"log(")
        return None

    def clearInput(self):
        self.Input_order.setText("")
        return None
    def clearAll(self):
        self.clearInput()
        self.history = ['','','','','']
        self.History.setText('')
        self.calc.ans = 0.0
        return None
    def deleteSymbol(self):
        self.Input_order.setText(self.Input_order.text()[:-1])
    def calculate_result(self):
        inp = self.Input_order.text()
        res = self.calc.run(inp)
        if not res is None:
            self.clearInput()
            
            self.history.append(str(res))
            self.history.pop(0)
            self.History.setText(self.history[0] +'\n'
                                +self.history[1] +'\n'
                                +self.history[2] +'\n'
                                +self.history[3] +'\n'
                                +"Ans = " + self.history[4])
        else:
            msg = QMessageBox()
            msg.setWindowTitle("")
            msg.setText("Input isn't correct")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()