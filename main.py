import sys
import webbrowser

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QByteArray, QBuffer, QEvent
from PySide6.QtGui import Qt, QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem

from Funcoes.data import DataAtual
from Views.ui_tela import Ui_MainWindow
from Crud.CrudDados import CrudDados
import pandas as pd


class Main(QMainWindow, Ui_MainWindow):
    #################################################
    ## Inicialização da classe Main
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #################################################

        #################################################
        # Populate the table
        self.populate_table_Widget()
        #################################################

        #################################################
        # Button to save
        self.ui.bt_salvar.clicked.connect(self.cadDados)
        # self.ui.bt_AddImagem.clicked.connect(self.)
        #################################################

        #################################################
        # Hour in Label
        data = DataAtual()
        data.diaAtual()
        self.ui.lb_Data.setText(data.diames)
        self.ui.lb_DiaSemana.setText(data.diasemana)
        #################################################

    def populate_table_Widget(self):


        self.ui.tb_Dados.clear()
        self.ui.tb_Dados.setColumnCount(3)

        item = QtWidgets.QTableWidgetItem()
        self.ui.tb_Dados.setHorizontalHeaderItem(0, item)
        item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        item = QtWidgets.QTableWidgetItem()
        self.ui.tb_Dados.setHorizontalHeaderItem(1, item)
        item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        item = QtWidgets.QTableWidgetItem()
        self.ui.tb_Dados.setHorizontalHeaderItem(2, item)
        item.setTextAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)  #############################

        self.columnLabels = ["ID", "A", "B"]
        self.ui.tb_Dados.setHorizontalHeaderLabels(self.columnLabels)

        self.ui.tb_Dados.verticalHeader().setVisible(True)
        self.ui.tb_Dados.verticalHeader().setDefaultSectionSize(30)
        self.ui.tb_Dados.verticalHeader().setMinimumSectionSize(15)
        self.ui.tb_Dados.horizontalHeader().setDefaultSectionSize(100)
        self.ui.tb_Dados.horizontalHeader().setMinimumSectionSize(35)
        self.ui.tb_Dados.alternatingRowColors()

        self.ui.tb_Dados.setColumnWidth(1, 150)
        self.ui.tb_Dados.setColumnWidth(2, 150)
        self.ui.tb_Dados.setColumnWidth(3, 200)
        self.ui.tb_Dados.setColumnWidth(4, 100)
        # self.ui.tb_Dados.selectionModel().currentIndex().siblingAtColumn(0).data()

        self.ui.tb_Dados.doubleClicked.connect(
            self.mouseDoubleClickEvent)  # https: // stackoverflow.com / questions / 4324005 / how - to - detect - doubleclick - in -qtableview

        self.PreencherTabela()
        self.clearCampos()

    def mouseDoubleClickEvent(self, e):
#DSDDSDSD
        if not self.ui.tx_A.text() and not self.ui.tx_B.text():

            for idx in self.ui.tb_Dados.selectionModel().selectedIndexes():
                self.ui.tx_A.setText(str(idx.row()))
                self.ui.tx_B.setText(str(idx.column()))

            """for column, label in [(0, self.ui.tx_A), (1, self.ui.tx_B)]:
                sibling = self.ui.tb_Dados.item(e.row(), column)
                self.ui.tx_A.setText(sibling)
"""
    def clearCampos(self):

        self.ui.tx_A.clear()
        self.ui.tx_B.clear()

    def PreencherTabela(self):

        lista = CrudDados()
        lista.listaDados()

        """
        if lista.imagem:
            pixmap = QPixmap()
            pixmap.loadFromData(
                QByteArray.fromBase64(lista.imagem))
            self.ui.lb_FotoProduto.setPixmap(pixmap.scaledToWidth(
                70, Qt.TransformationMode(Qt.FastTransformation)))
            # self.lb_FotoProduto.setScaledContents(True)
"""

        ###############################
        i = 0
        while self.ui.tb_Dados.rowCount() > 0:
            self.ui.tb_Dados.removeRow(0)

        if len(lista.a) >= 1:
            while i < len(lista.a):
                self.ui.tb_Dados.insertRow(i)

                self.CampoID(self.ui.tb_Dados, i, 0, lista.id[i])
                self.CampoNome(self.ui.tb_Dados, i, 1, lista.a[i])
                self.CampoNome(self.ui.tb_Dados, i, 2, lista.b[i])

                i += 1
            pass

    def CampoID(self, tabela, row, col, id):
        item = QtWidgets.QLabel()
        item.setAlignment(Qt.AlignBottom | Qt.AlignHCenter | Qt.AlignVCenter)
        item.setMargin(0)
        item.setStyleSheet('background: #FFF;')
        html = ("""
                  <span style="font-family:'Arial'; font-size:15px; 
                  font-weight: bold;color:#7AB32E ">{}</span><br/>
                  """).format(id)
        item.setText(html)
        tabela.setCellWidget(row, col, item)

        ################################

    def CampoNome(self, tabela, row, col, nome):
        item = QtWidgets.QLabel()
        item.setAlignment(Qt.AlignLeft | Qt.AlignBaseline)
        item.setIndent(3)
        item.setMargin(0)
        item.setStyleSheet("background:#FFF")
        html = (("""
           <span style="font-family:'Arial';font-size:15px;">{}</span><br/>
           """
                 )).format(nome)
        item.setText(html)
        tabela.setCellWidget(row, col, item)

    def cadDados(self):

        inserir = CrudDados()
        inserir.a = self.ui.tx_A.text().upper()
        inserir.b = self.ui.tx_B.text().upper()

        """
            # Função para inserir imagem
            if self.ui.lb_FotoProduto.pixmap():
                imagem = QPixmap(self.ui.lb_FotoProduto.pixmap())
                data = QByteArray()
                buf = QBuffer(data)
                imagem.save(buf, 'PNG')
                INSERI.imagem = str(data.toBase64()).encode('utf8')[2:-1]
            else:
                INSERI.imagem = False
"""
        inserir.inserirDado()
        self.populate_table_Widget()

    def ultimoId(self):

        last = CrudDados()
        last.lastIdDado()
        self.ui.tb_Dados.clear()
        self.PreencherTabela()

    # Imprimindo em pdf
    def previaImpressao(self, arg):
        self.documento.page().printToPdf(self.resourcepath('report.pdf'))
        self.documento.page().pdfPrintingFinished.connect(self.okPrinter)

    # Função executada após a impresso em pdf concluida
    def okPrinter(self, sucess):
        webbrowser.open_new_tab(self.resourcepath('report.pdf'))
        pass

    def UploadImagem(self):
        Dialog = QFileDialog()
        Dialog.setOption(QFileDialog.DontUseNativeDialog, True)

        fname = Dialog.getOpenFileName(
            self, "Selecionar Imagem", "", "Image files (*.jpg *.png)")[0]

        self.ui.lb_FotoProduto.setPixmap(QPixmap(fname).scaledToWidth(
            150, Qt.TransformationMode(Qt.FastTransformation)))
        # self.lb_FotoProduto.setScaledContents(True)

    def DelImagem(self):
        self.ui.lb_FotoProduto.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ##
    ########################################################################
    window = Main()
    window.show()
    sys.exit(app.exec())
