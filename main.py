"""
Основной скрипт программы.
Запускает конфигуратор окна, подключает слоты и отображает окно.
"""
# Импортируем системый модуль для корректного закрытия программы
import sys
# Импортируем минимальный набор виджетов
from PyQt5.QtWidgets import QApplication, QWidget
# Импортируем созданный нами класс со слотами
from slots import MainWindowSlots


# Создаём ещё один класс, наследуясь от класса со слотами
class MainWindow(MainWindowSlots):

    # При инициализации класса нам необходимо выпонить некоторые операции
    def __init__(self, form):
        # Сконфигурировать интерфейс методом из базового класса Ui_Form
        self.setupUi(form)
        # Подключить созданные нами слоты к виджетам
        self.connect_slots()

    # Подключаем слоты к виджетам
    def connect_slots(self):
        self.number_pi_b.clicked.connect(self.numberPiClicked)
        self.number_e_b.clicked.connect(self.number_e_clicked)
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

        self.delete_all.clicked.connect(self.clear_input)
        self.delete_symbol.clicked.connect(self.del_symbol)
        self.result.clicked.connect(self.calculate_result)
        return None

if __name__ == '__main__':
    # Создаём экземпляр приложения
    app = QApplication(sys.argv)
    # Создаём базовое окно, в котором будет отображаться наш UI
    window = QWidget()
    # Создаём экземпляр нашего UI
    ui = MainWindow(window)
    # Отображаем окно
    window.show()
    # Обрабатываем нажатие на кнопку окна "Закрыть"
    sys.exit(app.exec_())