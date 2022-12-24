"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets


import b_systeminfo_widget
import c_weatherapi_widget

class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):

        self.systemInfo = b_systeminfo_widget.Window(self)
        self.systemInfo.show()
        self.weatherApi = c_weatherapi_widget.Window(self)
        self.weatherApi.move(0, 140)
        self.weatherApi.show()

        # mainLayout = QtWidgets.QVBoxLayout()
        # mainLayout.addWidget(self.systemInfo)
        # mainLayout.addWidget(self.weatherApi)

        self.setFixedSize(300, 440)


if __name__ =='__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
