import sys
from intefazAutomata import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Ventana(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.aleatorio.clicked.connect(self.imprimir)

    def imprimir(self):
        text = self.ui.automata_text.text()
        auto = list()
        for i in text:
            auto.append(int(i))
        print(auto)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show()
    sys.exit(app.exec_())
