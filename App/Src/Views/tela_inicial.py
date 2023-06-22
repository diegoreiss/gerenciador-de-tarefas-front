# -*- coding: utf-8 -*-
import os

################################################################################
## Form generated from reading UI file 'tela_inicial.ui'
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
                               QHBoxLayout, QHeaderView, QLabel, QLineEdit,
                               QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
                               QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
                               QTextEdit, QToolButton, QVBoxLayout, QWidget)
from . import tela_login
from ..Routers.usuario_router import UsuarioRouter

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.main_window = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 60))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_logo = QFrame(self.Top_Bar)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setMaximumSize(QSize(80, 60))
        self.frame_logo.setStyleSheet(u"background-color: rgb(27, 68, 120);")
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_logo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_logo = QPushButton(self.frame_logo)
        self.btn_logo.setObjectName(u"btn_logo")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_logo.sizePolicy().hasHeightForWidth())
        self.btn_logo.setSizePolicy(sizePolicy)
        self.btn_logo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                    "border: 0px solid;")

        self.verticalLayout_2.addWidget(self.btn_logo)

        self.horizontalLayout.addWidget(self.frame_logo)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_logo = QLabel(self.frame_top)
        self.lbl_logo.setObjectName(u"lbl_logo")
        font = QFont()
        font.setPointSize(36)
        self.lbl_logo.setFont(font)
        self.lbl_logo.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbl_logo.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lbl_logo)

        self.horizontalLayout.addWidget(self.frame_top)

        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(80, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_tarefas = QPushButton(self.frame_top_menus)
        self.btn_page_tarefas.setObjectName(u"btn_page_tarefas")
        self.btn_page_tarefas.setMinimumSize(QSize(0, 40))
        self.btn_page_tarefas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_tarefas.setStyleSheet(u"QPushButton {\n"
                                            "	color: rgb(255, 255, 255);\n"
                                            "	background-color: rgb(35, 35, 35);\n"
                                            "	border: 0px solid;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "	background-color: rgb(85, 170, 255);\n"
                                            "\n"
                                            "	background-color: rgb(27, 68, 120);\n"
                                            "}")

        self.verticalLayout_4.addWidget(self.btn_page_tarefas)

        self.btn_page_conta = QPushButton(self.frame_top_menus)
        self.btn_page_conta.setObjectName(u"btn_page_conta")
        self.btn_page_conta.setMinimumSize(QSize(0, 40))
        self.btn_page_conta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_conta.setStyleSheet(u"QPushButton {\n"
                                          "	color: rgb(255, 255, 255);\n"
                                          "	background-color: rgb(35, 35, 35);\n"
                                          "	border: 0px solid;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "	background-color: rgb(85, 170, 255);\n"
                                          "\n"
                                          "	background-color: rgb(27, 68, 120);\n"
                                          "}")

        self.verticalLayout_4.addWidget(self.btn_page_conta)

        self.verticalSpacer = QSpacerItem(20, 4000, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.btn_page_sair = QPushButton(self.frame_top_menus)
        self.btn_page_sair.setObjectName(u"btn_page_sair")
        self.btn_page_sair.setMinimumSize(QSize(0, 40))
        self.btn_page_sair.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_sair.setStyleSheet(u"QPushButton {\n"
                                         "	color: rgb(255, 255, 255);\n"
                                         "	background-color: rgb(35, 35, 35);\n"
                                         "	border: 0px solid;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "	background-color: rgb(85, 170, 255);\n"
                                         "\n"
                                         "	background-color: rgb(27, 68, 120);\n"
                                         "}")

        self.verticalLayout_4.addWidget(self.btn_page_sair)

        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_tarefas = QWidget()
        self.page_tarefas.setObjectName(u"page_tarefas")
        self.verticalLayout_7 = QVBoxLayout(self.page_tarefas)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lbl_tarefas = QLabel(self.page_tarefas)
        self.lbl_tarefas.setObjectName(u"lbl_tarefas")
        font1 = QFont()
        font1.setPointSize(26)
        self.lbl_tarefas.setFont(font1)
        self.lbl_tarefas.setStyleSheet(u"color: #FFF;")
        self.lbl_tarefas.setAlignment(Qt.AlignRight | Qt.AlignTop | Qt.AlignTrailing)

        self.verticalLayout_7.addWidget(self.lbl_tarefas)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_criar = QPushButton(self.page_tarefas)
        self.btn_criar.setObjectName(u"btn_criar")
        self.btn_criar.setMinimumSize(QSize(70, 70))
        self.btn_criar.setMaximumSize(QSize(70, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        self.btn_criar.setFont(font2)
        self.btn_criar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_criar.setStyleSheet(u"QPushButton {\n"
                                     "background-color: rgb(27, 68, 120);\n"
                                     "image: url(:/newTaskIcon/add task icon.png);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-radius: 35px;\n"
                                     "border:1px solid black;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "	\n"
                                     "	background-color: rgb(38, 97, 170);\n"
                                     "}\n"
                                     "QPushButton:pressed {\n"
                                     "	background-color: rgb(27, 68, 120);\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "")
        self.btn_criar.setIconSize(QSize(16, 16))
        self.btn_criar.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.btn_criar)

        self.btn_editar = QPushButton(self.page_tarefas)
        self.btn_editar.setObjectName(u"btn_editar")
        self.btn_editar.setMinimumSize(QSize(70, 70))
        self.btn_editar.setMaximumSize(QSize(70, 16777215))
        self.btn_editar.setFont(font2)
        self.btn_editar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editar.setStyleSheet(u"QPushButton {\n"
                                      "background-color: rgb(27, 68, 120);\n"
                                      "image: url(:/newTaskIcon/add task icon.png);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius: 35px;\n"
                                      "border:1px solid black;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "	\n"
                                      "	background-color: rgb(38, 97, 170);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "	background-color: rgb(27, 68, 120);\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "")
        self.btn_editar.setIconSize(QSize(16, 16))
        self.btn_editar.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.btn_editar)

        self.btn_deletar = QPushButton(self.page_tarefas)
        self.btn_deletar.setObjectName(u"btn_deletar")
        self.btn_deletar.setMinimumSize(QSize(70, 70))
        self.btn_deletar.setMaximumSize(QSize(70, 16777215))
        self.btn_deletar.setFont(font2)
        self.btn_deletar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_deletar.setStyleSheet(u"QPushButton {\n"
                                       "background-color: rgb(27, 68, 120);\n"
                                       "image: url(:/newTaskIcon/add task icon.png);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border-radius: 35px;\n"
                                       "border:1px solid black;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "	\n"
                                       "	background-color: rgb(38, 97, 170);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "	background-color: rgb(27, 68, 120);\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "")
        self.btn_deletar.setIconSize(QSize(16, 16))
        self.btn_deletar.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.btn_deletar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.tableWidget = QTableWidget(self.page_tarefas)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet(u"\n"
                                       "QHeaderView::section\n"
                                       "{\n"
                                       "background-color:rgb(27, 68, 120);\n"
                                       "color: white;\n"
                                       "};\n"
                                       "\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "border:1px solid rgb(27, 68, 120);\n"
                                       "")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(176)

        self.verticalLayout_7.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.page_tarefas)
        self.page_conta = QWidget()
        self.page_conta.setObjectName(u"page_conta")
        self.verticalLayout_6 = QVBoxLayout(self.page_conta)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_conta = QLabel(self.page_conta)
        self.lbl_conta.setObjectName(u"lbl_conta")
        self.lbl_conta.setMaximumSize(QSize(16777215, 50))
        self.lbl_conta.setFont(font1)
        self.lbl_conta.setStyleSheet(u"color: #FFF;")
        self.lbl_conta.setAlignment(Qt.AlignRight | Qt.AlignTop | Qt.AlignTrailing)

        self.verticalLayout_6.addWidget(self.lbl_conta)

        self.lbl_nome = QLabel(self.page_conta)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setMaximumSize(QSize(16777215, 20))
        font3 = QFont()
        font3.setPointSize(12)
        self.lbl_nome.setFont(font3)
        self.lbl_nome.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.lbl_nome)

        self.txt_nome = QLineEdit(self.page_conta)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setMaximumSize(QSize(700, 16777215))
        self.txt_nome.setFont(font3)
        self.txt_nome.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
                                    "border:1px solid black;\n"
                                    "border-radius:4px;\n"
                                    "color: rgb(195, 195, 195);")

        self.verticalLayout_6.addWidget(self.txt_nome)

        self.lbl_usuario = QLabel(self.page_conta)
        self.lbl_usuario.setObjectName(u"lbl_usuario")
        self.lbl_usuario.setFont(font3)
        self.lbl_usuario.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.lbl_usuario)

        self.txt_usuario = QLineEdit(self.page_conta)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setMaximumSize(QSize(700, 16777215))
        self.txt_usuario.setFont(font3)
        self.txt_usuario.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
                                       "border:1px solid black;\n"
                                       "border-radius:4px;\n"
                                       "color: rgb(195, 195, 195);")

        self.verticalLayout_6.addWidget(self.txt_usuario)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_conta)
        self.page_criacao = QWidget()
        self.page_criacao.setObjectName(u"page_criacao")
        self.page_criacao.setEnabled(True)
        self.verticalLayout_8 = QVBoxLayout(self.page_criacao)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lbl_criacao = QLabel(self.page_criacao)
        self.lbl_criacao.setObjectName(u"lbl_criacao")
        self.lbl_criacao.setMaximumSize(QSize(16777215, 50))
        self.lbl_criacao.setFont(font1)
        self.lbl_criacao.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbl_criacao.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.lbl_criacao)

        self.frame_mid = QFrame(self.page_criacao)
        self.frame_mid.setObjectName(u"frame_mid")
        self.frame_mid.setFrameShape(QFrame.StyledPanel)
        self.frame_mid.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_mid)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_mid_2 = QFrame(self.frame_mid)
        self.frame_mid_2.setObjectName(u"frame_mid_2")
        self.frame_mid_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_mid_2.sizePolicy().hasHeightForWidth())
        self.frame_mid_2.setSizePolicy(sizePolicy1)
        self.frame_mid_2.setFrameShape(QFrame.StyledPanel)
        self.frame_mid_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_mid_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.lbl_titulo_tarefa = QLabel(self.frame_mid_2)
        self.lbl_titulo_tarefa.setObjectName(u"lbl_titulo_tarefa")
        self.lbl_titulo_tarefa.setEnabled(False)

        self.verticalLayout_10.addWidget(self.lbl_titulo_tarefa)

        self.txt_titulo_tarefa = QLineEdit(self.frame_mid_2)
        self.txt_titulo_tarefa.setObjectName(u"txt_titulo_tarefa")
        self.txt_titulo_tarefa.setEnabled(True)
        self.txt_titulo_tarefa.setMinimumSize(QSize(60, 0))
        self.txt_titulo_tarefa.setMaximumSize(QSize(300, 16777215))
        self.txt_titulo_tarefa.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                             "background-color: rgb(35, 35, 35);\n"
                                             "border:1px solid black;")
        self.txt_titulo_tarefa.setDragEnabled(False)
        self.txt_titulo_tarefa.setReadOnly(False)

        self.verticalLayout_10.addWidget(self.txt_titulo_tarefa)

        self.horizontalLayout_6.addLayout(self.verticalLayout_10)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, -1, 5, -1)
        self.lbl_status_tarefa = QLabel(self.frame_mid_2)
        self.lbl_status_tarefa.setObjectName(u"lbl_status_tarefa")

        self.verticalLayout_11.addWidget(self.lbl_status_tarefa)

        self.comboBox_status_tarefa = QComboBox(self.frame_mid_2)
        self.comboBox_status_tarefa.addItem("")
        self.comboBox_status_tarefa.addItem("")
        self.comboBox_status_tarefa.setObjectName(u"comboBox_status_tarefa")
        self.comboBox_status_tarefa.setEnabled(True)
        self.comboBox_status_tarefa.setMinimumSize(QSize(100, 0))
        self.comboBox_status_tarefa.setMaximumSize(QSize(200, 16777215))
        self.comboBox_status_tarefa.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                                  "")
        self.comboBox_status_tarefa.setEditable(False)

        self.verticalLayout_11.addWidget(self.comboBox_status_tarefa)

        self.horizontalLayout_6.addLayout(self.verticalLayout_11)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, -1, 5, -1)
        self.lbl_prioridade = QLabel(self.frame_mid_2)
        self.lbl_prioridade.setObjectName(u"lbl_prioridade")
        self.lbl_prioridade.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_14.addWidget(self.lbl_prioridade)

        self.comboBox_prioridade = QComboBox(self.frame_mid_2)
        self.comboBox_prioridade.addItem("")
        self.comboBox_prioridade.addItem("")
        self.comboBox_prioridade.addItem("")
        self.comboBox_prioridade.setObjectName(u"comboBox_prioridade")
        self.comboBox_prioridade.setEnabled(True)
        self.comboBox_prioridade.setMinimumSize(QSize(100, 0))
        self.comboBox_prioridade.setMaximumSize(QSize(200, 16777215))
        self.comboBox_prioridade.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.comboBox_prioridade.setEditable(False)

        self.verticalLayout_14.addWidget(self.comboBox_prioridade)

        self.horizontalLayout_6.addLayout(self.verticalLayout_14)

        self.verticalLayout_13.addLayout(self.horizontalLayout_6)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lbl_descricao_tarefa = QLabel(self.frame_mid_2)
        self.lbl_descricao_tarefa.setObjectName(u"lbl_descricao_tarefa")

        self.verticalLayout_9.addWidget(self.lbl_descricao_tarefa)

        self.txt_descricao_tarefa = QPlainTextEdit(self.frame_mid_2)
        self.txt_descricao_tarefa.setObjectName(u"txt_descricao_tarefa")
        self.txt_descricao_tarefa.setEnabled(True)
        self.txt_descricao_tarefa.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                "background-color: rgb(35, 35, 35);\n"
                                                "border:1px solid black;")

        self.verticalLayout_9.addWidget(self.txt_descricao_tarefa)

        self.verticalLayout_13.addLayout(self.verticalLayout_9)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 5, -1, -1)
        self.lbl_anexo_professor = QLabel(self.frame_mid_2)
        self.lbl_anexo_professor.setObjectName(u"lbl_anexo_professor")

        self.verticalLayout_12.addWidget(self.lbl_anexo_professor)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_anexo = QCommandLinkButton(self.frame_mid_2)
        self.btn_anexo.setObjectName(u"btn_anexo")
        self.btn_anexo.setEnabled(True)
        self.btn_anexo.setMaximumSize(QSize(16777215, 60))
        self.btn_anexo.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/clip/transferir.jfif", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_anexo.setIcon(icon)
        self.btn_anexo.setIconSize(QSize(25, 30))

        self.horizontalLayout_7.addWidget(self.btn_anexo)

        self.txt_anexo = QLineEdit(self.frame_mid_2)
        self.txt_anexo.setObjectName(u"txt_anexo")
        self.txt_anexo.setEnabled(False)
        self.txt_anexo.setMaximumSize(QSize(16777215, 16777215))
        self.txt_anexo.setAutoFillBackground(False)
        self.txt_anexo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(35, 35, 35);\n"
                                     "border:1px solid black;")

        self.horizontalLayout_7.addWidget(self.txt_anexo)

        self.btn_download_anexo_professor = QToolButton(self.frame_mid_2)
        self.btn_download_anexo_professor.setObjectName(u"btn_download_anexo_professor")
        self.btn_download_anexo_professor.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/download/download_icon.jfif", QSize(), QIcon.Normal, QIcon.On)
        self.btn_download_anexo_professor.setIcon(icon1)

        self.horizontalLayout_7.addWidget(self.btn_download_anexo_professor)

        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_10 = QLabel(self.frame_mid_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 17))

        self.verticalLayout_15.addWidget(self.label_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_anexo_aluno = QCommandLinkButton(self.frame_mid_2)
        self.btn_anexo_aluno.setObjectName(u"btn_anexo_aluno")
        self.btn_anexo_aluno.setEnabled(True)
        self.btn_anexo_aluno.setMaximumSize(QSize(16777215, 60))
        self.btn_anexo_aluno.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_anexo_aluno.setIcon(icon)
        self.btn_anexo_aluno.setIconSize(QSize(25, 30))

        self.horizontalLayout_11.addWidget(self.btn_anexo_aluno)

        self.txt_anexo_aluno = QLineEdit(self.frame_mid_2)
        self.txt_anexo_aluno.setObjectName(u"txt_anexo_aluno")
        self.txt_anexo_aluno.setEnabled(False)
        self.txt_anexo_aluno.setMaximumSize(QSize(16777215, 16777215))
        self.txt_anexo_aluno.setAutoFillBackground(False)
        self.txt_anexo_aluno.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(35, 35, 35);\n"
                                           "border:1px solid black;")

        self.horizontalLayout_11.addWidget(self.txt_anexo_aluno)

        self.btn_download_anexo_aluno = QToolButton(self.frame_mid_2)
        self.btn_download_anexo_aluno.setObjectName(u"btn_download_anexo_aluno")
        self.btn_download_anexo_aluno.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_download_anexo_aluno.setIcon(icon1)

        self.horizontalLayout_11.addWidget(self.btn_download_anexo_aluno)

        self.verticalLayout_15.addLayout(self.horizontalLayout_11)

        self.verticalLayout_13.addLayout(self.verticalLayout_15)

        self.horizontalLayout_5.addWidget(self.frame_mid_2)

        self.frame_right = QFrame(self.frame_mid)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setMinimumSize(QSize(250, 0))
        self.frame_right.setMaximumSize(QSize(80, 16777215))
        self.frame_right.setFrameShape(QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_right)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.lbl_comentarios = QLabel(self.frame_right)
        self.lbl_comentarios.setObjectName(u"lbl_comentarios")

        self.verticalLayout_16.addWidget(self.lbl_comentarios)

        self.txt_comentarios_publicados = QTextEdit(self.frame_right)
        self.txt_comentarios_publicados.setObjectName(u"txt_comentarios_publicados")
        self.txt_comentarios_publicados.setEnabled(False)
        self.txt_comentarios_publicados.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                      "background-color: rgb(35, 35, 35);\n"
                                                      "border:1px solid black;")

        self.verticalLayout_16.addWidget(self.txt_comentarios_publicados)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 5, -1, -1)
        self.txt_comentario = QLineEdit(self.frame_right)
        self.txt_comentario.setObjectName(u"txt_comentario")
        self.txt_comentario.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(35, 35, 35);\n"
                                          "border:1px solid black;")

        self.horizontalLayout_12.addWidget(self.txt_comentario)

        self.btn_contario = QToolButton(self.frame_right)
        self.btn_contario.setObjectName(u"btn_contario")

        self.horizontalLayout_12.addWidget(self.btn_contario)

        self.verticalLayout_16.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_5.addWidget(self.frame_right)

        self.verticalLayout_8.addWidget(self.frame_mid)

        self.widget_foot = QWidget(self.page_criacao)
        self.widget_foot.setObjectName(u"widget_foot")
        self.widget_foot.setMinimumSize(QSize(0, 60))
        self.widget_foot.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_foot)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_publicar_tarefa = QPushButton(self.widget_foot)
        self.btn_publicar_tarefa.setObjectName(u"btn_publicar_tarefa")
        self.btn_publicar_tarefa.setEnabled(True)
        self.btn_publicar_tarefa.setMinimumSize(QSize(0, 30))
        self.btn_publicar_tarefa.setMaximumSize(QSize(200, 16777215))
        self.btn_publicar_tarefa.setFont(font3)
        self.btn_publicar_tarefa.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                               "background-color: rgb(35, 35, 35);\n"
                                               "border:1px solid black;")

        self.horizontalLayout_8.addWidget(self.btn_publicar_tarefa)

        self.verticalLayout_8.addWidget(self.widget_foot)

        self.stackedWidget.addWidget(self.page_criacao)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.horizontalLayout_2.addWidget(self.frame_pages)

        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(MainWindow)

        # me
        self.usuario_atual = self.get_usuario_atual()
        print(self.usuario_atual)
        self.btn_page_sair.clicked.connect(self.deslogar)
        self.btn_page_conta.clicked.connect(self.goto_tela_conta)
        self.configurar_tela_usuario()


    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_logo.setText(QCoreApplication.translate("MainWindow", u"LOGO", None))
        self.lbl_logo.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Teen's</span></p></body></html>",
                                                         None))
        self.btn_page_tarefas.setText(QCoreApplication.translate("MainWindow", u"Tarefas", None))
        self.btn_page_conta.setText(QCoreApplication.translate("MainWindow", u"Conta", None))
        self.btn_page_sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.lbl_tarefas.setText(QCoreApplication.translate("MainWindow",
                                                            u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">TAREFAS</span></p></body></html>",
                                                            None))
        self.btn_criar.setText("")
        self.btn_editar.setText("")
        self.btn_deletar.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Prioridade", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Anexo", None));
        self.lbl_conta.setText(QCoreApplication.translate("MainWindow",
                                                          u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">CONTA</span></p></body></html>",
                                                          None))
        self.lbl_nome.setText(QCoreApplication.translate("MainWindow", u"Nome Completo", None))
        self.lbl_usuario.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.lbl_criacao.setText(QCoreApplication.translate("MainWindow",
                                                            u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">CRIA\u00c7\u00c3O DE TAREFAS</span></p></body></html>",
                                                            None))
        self.lbl_titulo_tarefa.setText(QCoreApplication.translate("MainWindow",
                                                                  u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                  "p, li { white-space: pre-wrap; }\n"
                                                                  "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
                                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Titulo</span></p></body></html>",
                                                                  None))
        self.lbl_status_tarefa.setText(QCoreApplication.translate("MainWindow",
                                                                  u"<html><head/><body><p><span style=\" color:#ffffff;\">Status</span></p></body></html>",
                                                                  None))
        self.comboBox_status_tarefa.setItemText(0, QCoreApplication.translate("MainWindow", u"Ativo", None))
        self.comboBox_status_tarefa.setItemText(1, QCoreApplication.translate("MainWindow", u"Inativo", None))

        self.lbl_prioridade.setText(QCoreApplication.translate("MainWindow",
                                                               u"<html><head/><body><p><span style=\" color:#ffffff;\">Prioridade</span></p><p><span style=\" color:#ffffff;\"><br/></span></p></body></html>",
                                                               None))
        self.comboBox_prioridade.setItemText(0, QCoreApplication.translate("MainWindow", u"Alta", None))
        self.comboBox_prioridade.setItemText(1, QCoreApplication.translate("MainWindow", u"Media", None))
        self.comboBox_prioridade.setItemText(2, QCoreApplication.translate("MainWindow", u"Baixa", None))

        self.lbl_descricao_tarefa.setText(QCoreApplication.translate("MainWindow",
                                                                     u"<html><head/><body><p><span style=\" color:#ffffff;\">Descri\u00e7\u00e3o</span></p></body></html>",
                                                                     None))
        self.lbl_anexo_professor.setText(QCoreApplication.translate("MainWindow",
                                                                    u"<html><head/><body><p><span style=\" color:#ffffff;\">Material de Referencia</span></p></body></html>",
                                                                    None))
        self.btn_anexo.setText(QCoreApplication.translate("MainWindow", u"Anexo", None))
        self.btn_download_anexo_professor.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p><span style=\" color:#f5f5f5;\">Entregar</span></p><p><span style=\" color:#f5f5f5;\"><br/></span></p></body></html>",
                                                         None))
        self.btn_anexo_aluno.setText(QCoreApplication.translate("MainWindow", u"Anexo", None))
        self.btn_download_anexo_aluno.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lbl_comentarios.setText(QCoreApplication.translate("MainWindow",
                                                                u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Comentarios</span></p></body></html>",
                                                                None))
        self.btn_contario.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.btn_publicar_tarefa.setText(QCoreApplication.translate("MainWindow", u"Publicar", None))
    # retranslateUi

    def get_usuario_atual(self):
        try:
            usuario_router = UsuarioRouter()
            response = usuario_router.get_usuario_atual()

            return response.json()
        except BaseException as e:
            print(e)

    def deslogar(self):
        os.environ["TOKEN_USUARIO"] = ""
        os.environ["TOKEN_USUARIO_TYPE"] = ""

        self.window = QWidget()
        self.ui = tela_login.Ui_form_login()
        self.ui.setupUi(self.window)

        self.window.show()
        self.main_window.hide()

    def goto_tela_conta(self):
        self.stackedWidget.setCurrentWidget(self.page_conta)

    def preencher_tela_conta(self):
        nome_completo = f"{self.usuario_atual['nome']} {self.usuario_atual['sobrenome']}"
        self.txt_nome.setText(nome_completo)
        self.txt_usuario.setText(self.usuario_atual["nome_login"])

    def configurar_tela_usuario(self):
        self.preencher_tela_conta()
