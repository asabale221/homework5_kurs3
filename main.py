from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 

def add_lebel():
    print("Push Button")

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(400, 600, 400, 500)

    window.setWindowTitle("Hello world")
    main_text = QtWidgets.QLabel(window)
    main_text.setText("GeekAsabale")
    main_text.move(130, 199)

    btn = QtWidgets.QPushButton(window)
    btn.setText("Нажми")
    btn.clicked.connect(add_lebel)
    


    window.show()
    sys.exit(app.exec_())


application()