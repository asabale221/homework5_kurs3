from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
import sys

class From(QDialog):
    def __init__(self):
        super(From, self).__init__()

        loadUi('calc.ui', self)

        self.add.clicked.connect(self.add_num)
        self.sub.clicked.connect(self.sub_num)
        self.mult.clicked.connect(self.mult_num)
        self.div.clicked.connect(self.div_num)
    

    def add_num(self):
        num1 = self.input1.text()
        num2 = self.input2.text()
        self.result.setText(str(int(num1) + int(num2)))

    def sub_num(self):
        num1 = self.input1.text()
        num2 = self.input2.text()
        self.result.setText(str(int(num1) - int(num2)))

    def mult_num(self):
        num1 = self.input1.text()
        num2 = self.input2.text()
        self.result.setText(str(int(num1) * int(num2)))


    def div_num(self):
        try:
            num1 = self.input1.text()
            num2 = self.input2.text()
            self.result.setText(str(int(num1) / int(num2)))
        except ZeroDivisionError:
            self.result.setText("На нол делит нельзя")


app = QApplication(sys.argv)
form =From()
form.show()
app.exec_()