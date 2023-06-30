
import sys
from PySide6.QtCore import QtMsgType
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar

from Frm_ui import Ui_MainWindow

class FormPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
        self.btnCalcular.clicked.connect(self.exibir)
        
        self.show()
    
    def exibir(self):
        v1 = self.valor1.value()
        v2 = self.valor2.value()
        soma = v1 + v2
        self.resultado.setText(str(soma))
        
if __name__=="__main__":
    aplicacao = QApplication(sys.argv)
    janela = FormPrincipal()
    aplicacao.exec()