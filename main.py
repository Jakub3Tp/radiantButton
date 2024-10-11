import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.businessButton.toggled.connect(self.button_clicked)
        self.ui.firstButton.toggled.connect(self.button_clicked)
        self.ui.economicButton.toggled.connect(self.button_clicked)

        self.show()

    def button_clicked(self):
        price = 0
        if self.ui.economicButton.isChecked():
            price = 20
        elif self.ui.businessButton.isChecked():
            price = 150
        elif self.ui.firstButton.isChecked():
            price = 200
        else:
            price = 0
        self.ui.resultLabel.setText(f'Cena twojego lotu wynosi {price}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())