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
        self.number_pi_b.clicked.connect(self.number_pi_clicked)
        self.number_e_b.clicked.connect(self.number_e_clicked)
        self.number_0_b.clicked.connect(self.number_0_clicked)
        self.number_1_b.clicked.connect(self.number_1_clicked)
        self.number_2_b.clicked.connect(self.number_2_clicked)
        self.number_3_b.clicked.connect(self.number_3_clicked)
        self.number_4_b.clicked.connect(self.number_4_clicked)
        self.number_5_b.clicked.connect(self.number_5_clicked)
        self.number_6_b.clicked.connect(self.number_6_clicked)
        self.number_7_b.clicked.connect(self.number_7_clicked)
        self.number_8_b.clicked.connect(self.number_8_clicked)
        self.number_9_b.clicked.connect(self.number_9_clicked)
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