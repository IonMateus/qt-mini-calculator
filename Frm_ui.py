# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Frm.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(195, 279)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnCalcular = QPushButton(self.centralwidget)
        self.btnCalcular.setObjectName(u"btnCalcular")
        self.btnCalcular.setGeometry(QRect(40, 130, 120, 40))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btnCalcular.setFont(font)
        self.valor1 = QDoubleSpinBox(self.centralwidget)
        self.valor1.setObjectName(u"valor1")
        self.valor1.setGeometry(QRect(40, 10, 120, 40))
        font1 = QFont()
        font1.setPointSize(15)
        self.valor1.setFont(font1)
        self.valor2 = QDoubleSpinBox(self.centralwidget)
        self.valor2.setObjectName(u"valor2")
        self.valor2.setGeometry(QRect(40, 70, 120, 40))
        self.valor2.setFont(font1)
        self.resultado = QLineEdit(self.centralwidget)
        self.resultado.setObjectName(u"resultado")
        self.resultado.setGeometry(QRect(40, 190, 120, 40))
        self.resultado.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 195, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnCalcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
    # retranslateUi

