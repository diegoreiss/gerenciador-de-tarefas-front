# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_criar_conta.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QCommandLinkButton, QFrame,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget, QMessageBox)
from . import tela_login
from ..Routers.usuario_router import UsuarioRouter


class Ui_form_cadastro(object):
    def setupUi(self, form_cadastro):
        if not form_cadastro.objectName():
            form_cadastro.setObjectName(u"form_cadastro")
        form_cadastro.resize(399, 650)
        self.form_cadastro = form_cadastro
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form_cadastro.sizePolicy().hasHeightForWidth())
        form_cadastro.setSizePolicy(sizePolicy)
        form_cadastro.setMinimumSize(QSize(399, 650))
        form_cadastro.setMaximumSize(QSize(399, 650))
        form_cadastro.setStyleSheet(u"background-color: rgb(52, 52, 52);")
        self.verticalLayout = QVBoxLayout(form_cadastro)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(form_cadastro)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMinimumSize(QSize(0, 0))
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.main_frame)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 80))
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_top)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_subTitulo = QLabel(self.frame_top)
        self.lbl_subTitulo.setObjectName(u"lbl_subTitulo")

        self.verticalLayout_3.addWidget(self.lbl_subTitulo)

        self.lbl_titulo = QLabel(self.frame_top)
        self.lbl_titulo.setObjectName(u"lbl_titulo")

        self.verticalLayout_3.addWidget(self.lbl_titulo)

        self.verticalLayout_2.addWidget(self.frame_top)

        self.frame_mid = QFrame(self.main_frame)
        self.frame_mid.setObjectName(u"frame_mid")
        self.frame_mid.setMaximumSize(QSize(16777215, 366))
        self.frame_mid.setFrameShape(QFrame.StyledPanel)
        self.frame_mid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_mid)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.layout_nome = QVBoxLayout()
        self.layout_nome.setObjectName(u"layout_nome")
        self.lbl_nome = QLabel(self.frame_mid)
        self.lbl_nome.setObjectName(u"lbl_nome")

        self.layout_nome.addWidget(self.lbl_nome)

        self.txt_nome = QLineEdit(self.frame_mid)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(35, 35, 35);\n"
                                    "border:1px solid black;")

        self.layout_nome.addWidget(self.txt_nome)

        self.verticalLayout_9.addLayout(self.layout_nome)

        self.layout_sobrenome = QVBoxLayout()
        self.layout_sobrenome.setObjectName(u"layout_sobrenome")
        self.lbl_sobrenome = QLabel(self.frame_mid)
        self.lbl_sobrenome.setObjectName(u"lbl_sobrenome")

        self.layout_sobrenome.addWidget(self.lbl_sobrenome)

        self.txt_sobrenome = QLineEdit(self.frame_mid)
        self.txt_sobrenome.setObjectName(u"txt_sobrenome")
        self.txt_sobrenome.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(35, 35, 35);\n"
                                         "border:1px solid black;")

        self.layout_sobrenome.addWidget(self.txt_sobrenome)

        self.verticalLayout_9.addLayout(self.layout_sobrenome)

        self.layout_username = QVBoxLayout()
        self.layout_username.setObjectName(u"layout_username")
        self.lbl_username = QLabel(self.frame_mid)
        self.lbl_username.setObjectName(u"lbl_username")

        self.layout_username.addWidget(self.lbl_username)

        self.txt_username = QLineEdit(self.frame_mid)
        self.txt_username.setObjectName(u"txt_username")
        self.txt_username.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(35, 35, 35);\n"
                                        "border:1px solid black;")

        self.layout_username.addWidget(self.txt_username)

        self.verticalLayout_9.addLayout(self.layout_username)

        self.layout_senha = QVBoxLayout()
        self.layout_senha.setObjectName(u"layout_senha")
        self.lbl_senha = QLabel(self.frame_mid)
        self.lbl_senha.setObjectName(u"lbl_senha")

        self.layout_senha.addWidget(self.lbl_senha)

        self.txt_senha = QLineEdit(self.frame_mid)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(35, 35, 35);\n"
                                     "border:1px solid black;")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.layout_senha.addWidget(self.txt_senha)

        self.verticalLayout_9.addLayout(self.layout_senha)

        self.verticalLayout_2.addWidget(self.frame_mid)

        self.frame_foot = QFrame(self.main_frame)
        self.frame_foot.setObjectName(u"frame_foot")
        self.frame_foot.setMaximumSize(QSize(16777215, 130))
        self.frame_foot.setMouseTracking(True)
        self.frame_foot.setFrameShape(QFrame.StyledPanel)
        self.frame_foot.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_foot)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 9)
        self.horizontalSpacer_3 = QSpacerItem(120, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.lbl_funcao = QLabel(self.frame_foot)
        self.lbl_funcao.setObjectName(u"lbl_funcao")
        self.lbl_funcao.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.lbl_funcao)

        self.comboBox_funcao = QComboBox(self.frame_foot)
        self.comboBox_funcao.addItem("")
        self.comboBox_funcao.addItem("")
        self.comboBox_funcao.addItem("")
        self.comboBox_funcao.setObjectName(u"comboBox_funcao")
        self.comboBox_funcao.setMaximumSize(QSize(110, 16777215))
        self.comboBox_funcao.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.comboBox_funcao)

        self.horizontalSpacer_2 = QSpacerItem(120, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_criar_conta = QPushButton(self.frame_foot)
        self.btn_criar_conta.setObjectName(u"btn_criar_conta")
        self.btn_criar_conta.setMinimumSize(QSize(0, 25))
        self.btn_criar_conta.setMaximumSize(QSize(120, 25))
        self.btn_criar_conta.setLayoutDirection(Qt.LeftToRight)
        self.btn_criar_conta.setStyleSheet(u"QPushButton {\n"
                                           "	color: rgb(255, 255, 255);\n"
                                           "	border:1px solid black;\n"
                                           "	background-color: rgb(27, 68, 120);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "	background-color:  rgb(50, 68, 120);\n"
                                           "}")

        self.horizontalLayout_2.addWidget(self.btn_criar_conta)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.btn_return = QCommandLinkButton(self.frame_foot)
        self.btn_return.setObjectName(u"btn_return")
        self.btn_return.setMinimumSize(QSize(0, 25))
        self.btn_return.setMaximumSize(QSize(120, 16777215))
        self.btn_return.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.btn_return)

        self.verticalLayout_2.addWidget(self.frame_foot)

        self.verticalLayout.addWidget(self.main_frame)

        self.retranslateUi(form_cadastro)

        QMetaObject.connectSlotsByName(form_cadastro)

        # me
        self.btn_return.clicked.connect(self.goto_tela_login)
        self.btn_criar_conta.clicked.connect(self.criar_conta)

    # setupUi

    def retranslateUi(self, form_cadastro):
        form_cadastro.setWindowTitle(QCoreApplication.translate("form_cadastro", u"Form", None))
        # if QT_CONFIG(tooltip)
        self.lbl_subTitulo.setToolTip(
            QCoreApplication.translate("form_cadastro", u"<html><head/><body><p><br/></p></body></html>", None))
        # endif // QT_CONFIG(tooltip)
        self.lbl_subTitulo.setText(QCoreApplication.translate("form_cadastro",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                                              "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#fefefe; vertical-align:super;\">Criar conta</span></p>\n"
                                                              "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; color:#fefefe; vertical-align:super;\"><br /></p></body></html>",
                                                              None))
        self.lbl_titulo.setText(QCoreApplication.translate("form_cadastro",
                                                           u"<html><head/><body><p align=\"center\"><span style=\" color:#fefefe;\">Preencha os dados de Cadastro.</span></p></body></html>",
                                                           None))
        self.lbl_nome.setText(QCoreApplication.translate("form_cadastro",
                                                         u"<html><head/><body><p><span style=\" color:#f0f0f0;\">Nome</span></p></body></html>",
                                                         None))
        self.lbl_sobrenome.setText(QCoreApplication.translate("form_cadastro",
                                                              u"<html><head/><body><p><span style=\" color:#fdfdfd;\">Sobrenome</span></p></body></html>",
                                                              None))
        self.lbl_username.setText(QCoreApplication.translate("form_cadastro",
                                                             u"<html><head/><body><p><span style=\" color:#ffffff;\">Nome de usu\u00e1rio</span></p></body></html>",
                                                             None))
        self.lbl_senha.setText(QCoreApplication.translate("form_cadastro",
                                                          u"<html><head/><body><p><span style=\" color:#ffffff;\">Senha</span></p></body></html>",
                                                          None))
        self.lbl_funcao.setText(QCoreApplication.translate("form_cadastro",
                                                           u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Sua Fun\u00e7\u00e3o:</span></p></body></html>",
                                                           None))
        self.comboBox_funcao.setItemText(0, QCoreApplication.translate("form_cadastro", u"Selecione", None))
        self.comboBox_funcao.setItemText(1, QCoreApplication.translate("form_cadastro", u"Aluno", None))
        self.comboBox_funcao.setItemText(2, QCoreApplication.translate("form_cadastro", u"Professor", None))

        self.btn_criar_conta.setText(QCoreApplication.translate("form_cadastro", u"Criar conta", None))
        self.btn_return.setText(QCoreApplication.translate("form_cadastro", u"Voltar", None))

    # retranslateUi

    def goto_tela_login(self):
        self.window = QWidget()
        self.ui = tela_login.Ui_form_login()

        self.ui.setupUi(self.window)
        self.window.show()
        self.form_cadastro.hide()

    def get_campos(self):
        campos = {
            "nome": self.txt_nome.text(),
            "sobrenome": self.txt_sobrenome.text(),
            "nome_login": self.txt_username.text(),
            "senha_hash": self.txt_senha.text(),
            "funcao_id": self.comboBox_funcao.currentIndex()
        }

        return campos

    def limpar_campos(self):
        for qvb_child in self.frame_mid.children():
            for child in qvb_child.children():
                if isinstance(child, QLineEdit):
                    child.clear()
                elif isinstance(child, QComboBox):
                    child.setCurrentIndex(0)

    def is_campos_preenchidos(self):
        boolean = (len(self.txt_nome.text()) != 0
                   and len(self.txt_sobrenome.text()) != 0
                   and len(self.txt_username.text()) != 0
                   and len(self.txt_senha.text()) != 0
                   and self.comboBox_funcao.currentIndex() != 0)

        return boolean

    def criar_conta(self):
        campos_usuario = self.get_campos()
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Cadastro de Usuário")

        if self.is_campos_preenchidos():
            try:
                usuario_router = UsuarioRouter()
                response = usuario_router.create_usuario(campos_usuario)

                if response.status_code == 201:
                    msg_box.setText("Cadastro realizado com sucesso!")
                    self.goto_tela_login()
                elif response.status_code == 400:
                    mensagem_erro = response.json()["detail"]
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setText(mensagem_erro)
                else:
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setText("Um erro ocorreu ao tentar cadastrar o usuário!")
            except BaseException as e:
                print(e)
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText("Um erro ocorreu ao conectar no sistema, tente novamente!")
                self.limpar_campos()
        else:
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Preencha os campos!!!")

        msg_box.exec()
