from PySide6 import QtWidgets, QtCore

from a_threads import SystemInfo

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


        self.initTreads()
        self.initUI()
        self.initSignals()


    def initTreads(self):

        self.thread = SystemInfo()
        self.thread.start()

    def initUI(self):

        self.delaySpinBox = QtWidgets.QSpinBox()
        self.delaySpinBox.setRange(1, 60)
        self.delayLabel = QtWidgets.QLabel("Задержка обновления:")

        self.cpuLoad = QtWidgets.QLCDNumber()
        self.cpuLabel = QtWidgets.QLabel("Загрузка процессора:")
        self.ramLoad = QtWidgets.QLCDNumber()
        self.ramLabel = QtWidgets.QLabel("Использование памяти:")

        ramLayout = QtWidgets.QHBoxLayout()
        ramLayout.addWidget(self.ramLabel)
        ramLayout.addWidget(self.ramLoad)

        cpuLayout = QtWidgets.QHBoxLayout()
        cpuLayout.addWidget(self.cpuLabel)
        cpuLayout.addWidget(self.cpuLoad)

        delayLayout = QtWidgets.QHBoxLayout()
        delayLayout.addWidget(self.delayLabel)
        delayLayout.addWidget(self.delaySpinBox)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addLayout(delayLayout)
        mainLayout.addLayout(cpuLayout)
        mainLayout.addLayout(ramLayout)

        self.setLayout(mainLayout)

        self.setMinimumSize(300, 120)

    def initSignals(self):
        self.delaySpinBox.valueChanged.connect(lambda x: self.thread.setDelay(x))
        self.thread.systemInfoReceived.connect(self.onSystemInfoReceived)

    def onSystemInfoReceived(self, info):

        self.cpuLoad.display(f"{info[0]}")
        self.ramLoad.display(f"{info[1]}")

    def closeEvent(self, event: QtCore.QEvent) -> None:

        self.thread.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()






"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
