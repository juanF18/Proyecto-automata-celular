import sys
import numpy as np
import time
from interfaz.interfazAutomata import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Ventana(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.aleatorio.clicked.connect(self.Aleatorio)
        self.ui.ejecutar.clicked.connect(self.Ejecutar)

    def Aleatorio(self):
        x = np.random.randint(255)
        y = self.ui.instrumento1.currentText()
        self.ui.automata_text.setText(str(x))
        print(y)

    def Ejecutar(self):
        if self.ui.automata_text.text() != None:
            from automataPygame.automata2 import ejecutar_pygame
            ejecutar_pygame(int(self.ui.automata_text.text()))


if __name__ == '__main__':
    app = QApplication([])
    window = Ventana()
    window.show()
    sys.exit(app.exec_())
