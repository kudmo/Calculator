import sys
from PyQt5.QtWidgets import QApplication, QWidget
from slots import MainWindowSlots

class MainWindow(MainWindowSlots):

    def __init__(self, form):
        self.is_history_window_open = False
        self.setupUi(form)
        self.connect_slots()
        
    def connect_slots(self):
        self.number_pi_b.clicked.connect(self.numberPiClicked)
        self.number_e_b.clicked.connect(self.numberEilerClicked)
        self.number_0_b.clicked.connect(self.numberZeroClicked)
        self.number_1_b.clicked.connect(self.numberOneClicked)
        self.number_2_b.clicked.connect(self.numberTwoClicked)
        self.number_3_b.clicked.connect(self.numberThreeClicked)
        self.number_4_b.clicked.connect(self.numberFourClicked)
        self.number_5_b.clicked.connect(self.numberFiveClicked)
        self.number_6_b.clicked.connect(self.numberSixClicked)
        self.number_7_b.clicked.connect(self.numberSevenClicked)
        self.number_8_b.clicked.connect(self.numberEightClicked)
        self.number_9_b.clicked.connect(self.numberNineClicked)

        self.operation_plus.clicked.connect(self.operationPlusClicked)
        self.operation_minus.clicked.connect(self.operationMinusClicked)
        self.operation_multiply.clicked.connect(self.operationMultiplyClicked)
        self.operation_devide.clicked.connect(self.operationDevideClicked)
        self.operation_exp.clicked.connect(self.operationExpClicked)

        self.brace_abs.clicked.connect(self.absBraces)
        self.brace_left.clicked.connect(self.leftBrace)
        self.brace_right.clicked.connect(self.rightBrace)

        self.function_sin.clicked.connect(self.funcSinClicked)
        self.function_cos.clicked.connect(self.funcCosClicked)
        self.function_tg.clicked.connect(self.funcTgClicked)
        self.function_log.clicked.connect(self.funcLogClicked)

        self.delete_all.clicked.connect(self.clearAll)
        self.delete_symbol.clicked.connect(self.deleteSymbol)
        self.ans_b.clicked.connect(self.ansButtonClicked)
        self.result.clicked.connect(self.calculateResult)


        self.input_order.setFocus()
        self.input_order.returnPressed.connect(self.result.click)
        return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Calculator')
    ui = MainWindow(window)
    window.show()
    ret = app.exec_()
    sys.exit(ret)