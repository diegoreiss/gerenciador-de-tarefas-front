# -*- coding: utf-8 -*-
import os

################################################################################
## Form generated from reading UI file 'tela_login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFrame, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget, QMessageBox)
from . import tela_criar_conta
from ..Routers.login_router import LoginRouter


class Ui_form_login(object):
    def setupUi(self, form_login):
        if not form_login.objectName():
            form_login.setObjectName(u"form_login")
        form_login.resize(399, 650)
        self.form_login = form_login
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form_login.sizePolicy().hasHeightForWidth())
        form_login.setSizePolicy(sizePolicy)
        form_login.setMinimumSize(QSize(399, 650))
        form_login.setMaximumSize(QSize(399, 650))
        form_login.setStyleSheet(u"background-color: rgb(52, 52, 52);")
        self.verticalLayout_2 = QVBoxLayout(form_login)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_top = QFrame(form_login)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 200))
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_top)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_titulo = QLabel(self.frame_top)
        self.lbl_titulo.setObjectName(u"lbl_titulo")

        self.verticalLayout.addWidget(self.lbl_titulo)

        self.lbl_bemVindo = QLabel(self.frame_top)
        self.lbl_bemVindo.setObjectName(u"lbl_bemVindo")

        self.verticalLayout.addWidget(self.lbl_bemVindo)

        self.verticalLayout_2.addWidget(self.frame_top)

        self.frame_mid = QFrame(form_login)
        self.frame_mid.setObjectName(u"frame_mid")
        self.frame_mid.setFrameShape(QFrame.StyledPanel)
        self.frame_mid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_mid)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_username = QLabel(self.frame_mid)
        self.lbl_username.setObjectName(u"lbl_username")
        self.lbl_username.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.lbl_username)

        self.txt_username = QLineEdit(self.frame_mid)
        self.txt_username.setObjectName(u"txt_username")
        self.txt_username.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(35, 35, 35);\n"
                                        "border:1px solid black;")

        self.verticalLayout_3.addWidget(self.txt_username)

        self.lbl_senha = QLabel(self.frame_mid)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setMinimumSize(QSize(0, 40))
        self.lbl_senha.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_3.addWidget(self.lbl_senha)

        self.txt_senha = QLineEdit(self.frame_mid)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setMinimumSize(QSize(0, 0))
        self.txt_senha.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(35, 35, 35);\n"
                                     "border:1px solid black;")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.txt_senha)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_login = QPushButton(self.frame_mid)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(0, 25))
        self.btn_login.setStyleSheet(u"QPushButton {\n"
                                     "	color: rgb(255, 255, 255);\n"
                                     "	border:1px solid black;\n"
                                     "	background-color: rgb(27, 68, 120);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "	background-color: rgb(50, 68, 120);\n"
                                     "}")

        self.verticalLayout_3.addWidget(self.btn_login)

        self.verticalLayout_2.addWidget(self.frame_mid)

        self.frame_foot = QFrame(form_login)
        self.frame_foot.setObjectName(u"frame_foot")
        self.frame_foot.setMinimumSize(QSize(0, 200))
        self.frame_foot.setFrameShape(QFrame.StyledPanel)
        self.frame_foot.setFrameShadow(QFrame.Raised)
        self.clb_criarConta = QCommandLinkButton(self.frame_foot)
        self.clb_criarConta.setObjectName(u"clb_criarConta")
        self.clb_criarConta.setGeometry(QRect(10, 20, 291, 48))
        self.clb_criarConta.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.frame_foot)

        self.frame_mid.raise_()
        self.frame_top.raise_()
        self.frame_foot.raise_()

        self.retranslateUi(form_login)

        QMetaObject.connectSlotsByName(form_login)

        # me

        self.clb_criarConta.clicked.connect(self.goto_tela_criar_conta)
        self.btn_login.clicked.connect(self.logar)

    # setupUi

    def retranslateUi(self, form_login):
        form_login.setWindowTitle(QCoreApplication.translate("form_login", u"Form", None))
        # if QT_CONFIG(tooltip)
        self.lbl_titulo.setToolTip(
            QCoreApplication.translate("form_login", u"<html><head/><body><p><br/></p></body></html>", None))
        # endif // QT_CONFIG(tooltip)
        self.lbl_titulo.setText(QCoreApplication.translate("form_login",
                                                           u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#fff8fb; vertical-align:super;\">Teen's</span></p></body></html>",
                                                           None))
        self.lbl_bemVindo.setText(QCoreApplication.translate("form_login",
                                                             u"<html><head/><body><p align=\"center\"><span style=\" color:#fafafa;\">Bem vindo! Preencha os dados de login.</span></p></body></html>",
                                                             None))
        self.lbl_username.setText(QCoreApplication.translate("form_login",
                                                             u"<html><head/><body><p><span style=\" color:#ffffff;\">Usu\u00e1rio</span></p></body></html>",
                                                             None))
        self.lbl_senha.setText(QCoreApplication.translate("form_login",
                                                          u"<html><head/><body><p><span style=\" color:#f5f5f5;\">Senha</span></p></body></html>",
                                                          None))
        self.btn_login.setText(QCoreApplication.translate("form_login", u"Entrar", None))
        self.clb_criarConta.setText(QCoreApplication.translate("form_login", u"Ainda n\u00e3o tenho uma conta!", None))
    # retranslateUi

    def goto_tela_criar_conta(self):
        self.window = QWidget()
        self.ui = tela_criar_conta.Ui_form_cadastro()

        self.ui.setupUi(self.window)
        self.window.show()
        self.form_login.hide()

    def goto_tela_principal(self):
        pass

    def get_campos(self):
        campos = {
            "username": self.txt_username.text(),
            "password": self.txt_senha.text()
        }

        return campos

    def is_campos_preenchidos(self):
        boolean = (len(self.txt_username.text()) != 0
                   and len(self.txt_senha.text()) != 0)

        return boolean

    def logar(self):
        campos = self.get_campos()
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Login")

        if self.is_campos_preenchidos():
            try:
                login_router = LoginRouter()
                response = login_router.login(campos)

                if response.status_code == 200:
                    os.environ["TOKEN_USUARIO"] = response.json()["access_token"]
                    os.environ["TOKEN_USUARIO_TYPE"] = response.json()["token_type"]

                    msg_box.setText("Login efetuado com sucesso!")
                    msg_box.exec()

                elif response.status_code == 403:
                    msg_response = response.json()["detail"]
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setText(msg_response)
                    msg_box.exec()
            except BaseException as e:
                print(e)
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText("Um erro ocorreu ao tentar se conectar no sistema. Tente novamente!")
                msg_box.exec()

        else:
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Preencha os campos!!!")
            msg_box.exec()
