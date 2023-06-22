import sys
from PySide6.QtWidgets import QApplication, QWidget
from Src.Views import tela_login


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = tela_login.Ui_form_login()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWidget()

    widget.show()
    sys.exit(app.exec())
  
