import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QMessageBox


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQt tuts!")
        self.setWindowIcon(QIcon("tux.png"))

        extract_action = QAction("&GET TO THE CHOPPAH!!!", self)
        extract_action.setShortcut("ctrl+Q")
        extract_action.setStatusTip("Leave The App")
        extract_action.triggered.connect(self.close_application)

        self.statusBar()

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("&File")
        file_menu.addAction(extract_action)

        self.home()

    def home(self):
        btn = QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(10, 70)

        extract_action = QAction(QIcon("exit.png"), 'Exit the Application', self)
        extract_action.triggered.connect(self.close_application)

        self.tool_bar = self.addToolBar("Extraction")
        self.tool_bar.addAction(extract_action)

        self.show()

    def close_application(self):
        choice = QMessageBox.question(self, "Quit!", "You Want Quit The Application?", QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Ok! Good Bye!")
            sys.exit()
        else:
            pass

    def closeEvent(self, event):
        event.ignore()
        self.close_application()


def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
