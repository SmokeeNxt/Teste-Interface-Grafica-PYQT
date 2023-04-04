import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLineEdit
from PyQt5 import QtGui


  #Gerando a Classe (JANELA MAIN)
###################################
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        loadUi("Conv.ui", self)
        #Caso eu queira mudar o titulo da janela: Devo escrever o nome + o comando para Setar o nome da janela, como escrito abaixo:
        #self.titulo = "Arthur"
        #self.setWindowTitle(self.titulo)
        self.pushButton_Converter.clicked.connect(self.Conversao)
        self.Recept_User_Money
 #################################
    def Conversao(self):
        conteudo = self.Recept_User_Money.text()
        isnum = conteudo.isnumeric()
        if isnum == False:
           self.label_Result.setText("Digite somente números!")
        else:
            dolar = 5.06 #no dia em que eu fiz, o dolar estava neste valor =)
            conta = float(conteudo) / dolar
            self.label_Result.setText(f"Resultado da Conversão: U${conta:.2f}")
        #print(conteudo)





    #Janela do Programa#
################################
app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec_())
################################


