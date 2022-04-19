from PyQt5.QtWidgets import QMessageBox
from form_ui import Ui_main_window
from calc_processor import Calculator
from history_window import HistoryWindow
class MainWindowSlots(Ui_main_window):
    calc = Calculator()
    def numberEilerClicked(self):
        self.input_order.setText(self.input_order.text()+" e ")
        self.input_order.setFocus()
        return None
    def numberPiClicked(self):
        self.input_order.setText(self.input_order.text()+" pi ")
        self.input_order.setFocus()
        return None
    def numberZeroClicked(self):
        self.input_order.setText(self.input_order.text()+"0")
        self.input_order.setFocus()
        return None
    def numberOneClicked(self):
        self.input_order.setText(self.input_order.text()+"1")
        self.input_order.setFocus()
        return None
    def numberTwoClicked(self):
        self.input_order.setText(self.input_order.text()+"2")
        self.input_order.setFocus()
        return None
    def numberThreeClicked(self):
        self.input_order.setText(self.input_order.text()+"3")
        self.input_order.setFocus()
        return None
    def numberFourClicked(self):
        self.input_order.setText(self.input_order.text()+"4")
        self.input_order.setFocus()
        return None
    def numberFiveClicked(self):
        self.input_order.setText(self.input_order.text()+"5")
        self.input_order.setFocus()
        return None
    def numberSixClicked(self):
        self.input_order.setText(self.input_order.text()+"6")
        self.input_order.setFocus()
        return None    
    def numberSevenClicked(self):
        self.input_order.setText(self.input_order.text()+"7")
        self.input_order.setFocus()
        return None
    def numberEightClicked(self):
        self.input_order.setText(self.input_order.text()+"8")
        self.input_order.setFocus()
        return None
    def numberNineClicked(self):
        self.input_order.setText(self.input_order.text()+"9")
        self.input_order.setFocus()
        return None
    
    def operationPlusClicked(self):
        self.input_order.setText(self.input_order.text()+" + ")
        self.input_order.setFocus()
        return None
    def operationMinusClicked(self):
        self.input_order.setText(self.input_order.text()+" - ")
        self.input_order.setFocus()
        return None
    def operationMultiplyClicked(self):
        self.input_order.setText(self.input_order.text()+" * ")
        self.input_order.setFocus()
        return None
    def operationDevideClicked(self):
        self.input_order.setText(self.input_order.text()+" / ")
        self.input_order.setFocus()
        return None
    def operationExpClicked(self):
        self.input_order.setText(self.input_order.text()+"^")
        self.input_order.setFocus()
        return None
    
    def absBraces(self):
        self.input_order.setText(self.input_order.text()+"|")
        self.input_order.setFocus()
        return None
    def leftBrace(self):
        self.input_order.setText(self.input_order.text()+"(")
        self.input_order.setFocus()
        return None
    def rightBrace(self):
        self.input_order.setText(self.input_order.text()+")")
        self.input_order.setFocus()
        return None
    
    def funcSinClicked(self):
        self.input_order.setText(self.input_order.text()+"sin(")
        self.input_order.setFocus()
        return None
    def funcCosClicked(self):
        self.input_order.setText(self.input_order.text()+"cos(")
        self.input_order.setFocus()
        return None
    def funcTgClicked(self):
        self.input_order.setText(self.input_order.text()+"tg(")
        self.input_order.setFocus()
        return None
    def funcLogClicked(self):
        self.input_order.setText(self.input_order.text()+"log(")
        self.input_order.setFocus()
        return None

    def clearInput(self):
        self.input_order.setText("")
        self.input_order.setFocus()
        return None
    def clearAll(self):
        self.clearInput()
        self.last_operation.setText('')
        self.calc.ans = 0.0
        self.input_order.setFocus()
        return None
    def deleteSymbol(self):
        self.input_order.setText(self.input_order.text()[:-1])
        self.input_order.setFocus()
        return None
    def ansButtonClicked(self):
        self.input_order.setText(self.input_order.text()+"Ans")
        self.input_order.setFocus()
        return None
    def show_history_window(self):
        if not self.is_history_window_open:
            self.history_window = HistoryWindow()
            self.history_window.setGeometry(500, 300, 300, 300)
            self.history_window.setWindowTitle('History')
            self.history_window.show()
            self.is_history_window_open = True
        self.history_window.addNewOrderInHistory(self.last_operation.text())

    def calculateResult(self):
        inp = self.input_order.text()
        if not inp=='':
            try:
                res = self.calc.run(inp)
                assert(not res is None)
                
                self.clearInput()
                self.last_operation.setText(str(inp) +' = '+ str(res) )
                self.show_history_window()
            except AssertionError:
                msg = QMessageBox()
                msg.setWindowTitle("")
                msg.setText("Input isn't correct")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
            except ZeroDivisionError:
                msg = QMessageBox()
                msg.setWindowTitle("")
                msg.setText("Devision by zero")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
            except:
                msg = QMessageBox()
                msg.setWindowTitle("")
                msg.setText("Something goes wrong")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
            self.input_order.setFocus()

        return None
