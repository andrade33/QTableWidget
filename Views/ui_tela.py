# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_teladjyLNI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(468, 372)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tx_A = QLineEdit(self.frame)
        self.tx_A.setObjectName(u"tx_A")
        self.tx_A.setGeometry(QRect(170, 7, 132, 21))
        self.tx_B = QLineEdit(self.frame)
        self.tx_B.setObjectName(u"tx_B")
        self.tx_B.setGeometry(QRect(170, 34, 132, 21))
        self.lab_A = QLabel(self.frame)
        self.lab_A.setObjectName(u"lab_A")
        self.lab_A.setGeometry(QRect(150, 10, 16, 16))
        self.lab_B = QLabel(self.frame)
        self.lab_B.setObjectName(u"lab_B")
        self.lab_B.setGeometry(QRect(150, 37, 16, 16))
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 0, 101, 36))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_DiaSemana = QLabel(self.frame_2)
        self.lb_DiaSemana.setObjectName(u"lb_DiaSemana")
        self.lb_DiaSemana.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lb_DiaSemana)

        self.lb_Data = QLabel(self.frame_2)
        self.lb_Data.setObjectName(u"lb_Data")
        self.lb_Data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lb_Data)

        self.tb_Dados = QTableWidget(self.frame)
        if (self.tb_Dados.columnCount() < 4):
            self.tb_Dados.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_Dados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_Dados.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_Dados.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_Dados.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tb_Dados.setObjectName(u"tb_Dados")
        self.tb_Dados.setGeometry(QRect(20, 130, 411, 192))
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(164, 60, 158, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_salvar = QPushButton(self.layoutWidget)
        self.bt_salvar.setObjectName(u"bt_salvar")

        self.horizontalLayout_2.addWidget(self.bt_salvar)

        self.bt_AddImagem = QPushButton(self.layoutWidget)
        self.bt_AddImagem.setObjectName(u"bt_AddImagem")

        self.horizontalLayout_2.addWidget(self.bt_AddImagem)

        self.lb_FotoProduto = QLabel(self.frame)
        self.lb_FotoProduto.setObjectName(u"lb_FotoProduto")
        self.lb_FotoProduto.setGeometry(QRect(340, 10, 81, 101))
        self.lb_FotoProduto.setStyleSheet(u"background-color: rgb(255, 85, 255);")

        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lab_A.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.lab_B.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lb_DiaSemana.setText(QCoreApplication.translate("MainWindow", u"Dia", None))
        self.lb_Data.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        ___qtablewidgetitem = self.tb_Dados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tb_Dados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem2 = self.tb_Dados.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem3 = self.tb_Dados.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Imagem", None));
        self.bt_salvar.setText(QCoreApplication.translate("MainWindow", u"Gravar", None))
        self.bt_AddImagem.setText(QCoreApplication.translate("MainWindow", u"Imagem", None))
        self.lb_FotoProduto.setText("")
    # retranslateUi

