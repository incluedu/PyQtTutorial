from PyQt5 import QtWidgets

from designer_test import Ui_MainWindow


def on_btn_clicked():
    print("btn1 clicked")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_2.clicked.connect(on_btn_clicked())

    MainWindow.show()
    sys.exit(app.exec_())

