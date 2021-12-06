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
        # colores para las notas

        self.colores = {
            "Do": (255, 0, 0),
            "Re": (0, 255, 0),
            "Mi": (0, 0, 255),
            "Fa": (255, 255, 0),
            "So": (255, 50, 255),
            "black": (0, 0, 0)
        }

        self.ui.aleatorio.clicked.connect(self.Aleatorio)
        self.ui.ejecutar.clicked.connect(self.Ejecutar)

    def Aleatorio(self):
        x = np.random.randint(255)
        w = self.ui.nota1.currentText()
        y = self.ui.instrumento1.currentText()
        self.ui.automata_text.setText(str(x))
        print(f'color: {self.colores[w]}')
        print(y)

    def Ejecutar(self):
        if self.ui.automata_text.text() != None:
            from automataPygame.automata2 import ejecutar_pygame

            if self.ui.nota1.currentText() != self.ui.nota2.currentText():
                ejecutar_pygame(int(self.ui.automata_text.text()), self.ui.instrumento1.currentText(),
                                self.ui.nota1.currentText(), self.ui.nota2.currentText(),
                                self.colores[self.ui.nota1.currentText()], self.colores[self.ui.nota2.currentText()])
            elif self.ui.nota1.currentText() == self.ui.nota2.currentText():
                ejecutar_pygame(int(self.ui.automata_text.text()), self.ui.instrumento1.currentText(),
                                self.ui.nota1.currentText(), self.ui.nota2.currentText(),
                                self.colores[self.ui.nota1.currentText()], self.colores['black'])


if __name__ == '__main__':
    app = QApplication([])
    window = Ventana()
    window.show()
    sys.exit(app.exec_())
