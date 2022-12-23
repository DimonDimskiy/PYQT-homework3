"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""

from PySide6 import QtWidgets, QtCore

from a_threads import WeatherHandler

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.initUi()
        self.initSignals()

    def initUi(self):

        self.delayInsert = QtWidgets.QSpinBox()
        self.delayInsert.setRange(1, 60)
        self.delayLabel = QtWidgets.QLabel("Частота обновления (c):")

        self.longitudeInsert = QtWidgets.QDoubleSpinBox()
        self.longitudeInsert.setRange(-180, 180)
        self.longitudeInsert.setValue(30)
        self.longitudeLabel = QtWidgets.QLabel('Долгота:')

        self.latitudeInsert = QtWidgets.QDoubleSpinBox()
        self.latitudeInsert.setRange(-90, 90)
        self.latitudeInsert.setValue(60)
        self.latitudeLabel = QtWidgets.QLabel('Широта:')

        self.pushButton = QtWidgets.QPushButton("Старт")
        self.pushButton.setCheckable(True)

        self.weatherInfo = QtWidgets.QPlainTextEdit()
        self.weatherInfo.setReadOnly(True)

        delayLayout = QtWidgets.QHBoxLayout()
        delayLayout.addWidget(self.delayLabel)
        delayLayout.addWidget(self.delayInsert)

        longitudeLayout = QtWidgets.QHBoxLayout()
        longitudeLayout.addWidget(self.longitudeLabel)
        longitudeLayout.addWidget(self.longitudeInsert)

        latitudeLayout = QtWidgets.QHBoxLayout()
        latitudeLayout.addWidget(self.latitudeLabel)
        latitudeLayout.addWidget(self.latitudeInsert)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addLayout(delayLayout)
        mainLayout.addLayout(longitudeLayout)
        mainLayout.addLayout(latitudeLayout)
        mainLayout.addWidget(self.pushButton)
        mainLayout.addWidget(self.weatherInfo)

        self.setLayout(mainLayout)

        self.setMinimumSize(300, 300)

    def initThreads(self):

        self.thread = WeatherHandler()

    def initSignals(self):

        self.pushButton.clicked.connect(self.onPushButtonClicked)
        # self.thread.started.connect(self.onThreadStarted)
        # self.thread.statusCodeReceived.connect(self.onStatusCodeReceived)
        # self.thread.weatherDataReceived.connect(self.onWeatherDateReceived)

    # def onStatusCodeReceived(self, value):
    #     print(f"code Received{value}")
    #     self.weatherInfo.appendPlainText(f"code Received{value}")

    def onPushButtonClicked(self, status: bool):
        print(status)
        if status:
            self.thread.payload["longitude"] = self.longitudeInsert.value()
            self.thread.payload["latitude"] = self.latitudeInsert.value()
            self.thread.setDelay(self.delayInsert.value())
            self.delayInsert.setEnabled(False)
            self.longitudeInsert.setEnabled(False)
            self.latitudeInsert.setEnabled(False)
            print(self.thread.payload)
            self.thread.run()
        else:
            self.thread.status = False



    def closeEvent(self, event: QtCore.QEvent) -> None:
        self.thread.quit()





if __name__ == "__main__":

    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
