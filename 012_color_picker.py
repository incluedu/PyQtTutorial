import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QMessageBox, QCheckBox, QProgressBar, \
    QLabel, QComboBox, QStyleFactory, QFontDialog, QCalendarWidget, QColorDialog


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

        font_choice_action = QAction(QIcon("font.png"), 'Choice A Font', self)
        font_choice_action.triggered.connect(self.font_choice)
        self.tool_bar.addAction(font_choice_action)

        color_choice_action = QAction(QIcon("baseball.png"), 'Change The Background Color a font', self)
        color_choice_action.triggered.connect(self.color_choice)
        self.tool_bar.addAction(color_choice_action)

        check_box = QCheckBox('Enlarge Window', self)
        check_box.stateChanged.connect(self.enlarge_window)
        check_box.move(10, 100)
        check_box.toggle()

        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 70, 250, 20)

        self.btn = QPushButton("Downaload", self)
        self.btn.move(200, 100)
        self.btn.clicked.connect(self.download)

        self.lbl_style_choice = QLabel("Windows Vista", self)

        combo_box = QComboBox(self)
        combo_box.addItem("Fusion")
        combo_box.addItem("Windows")
        combo_box.addItem("Windowsvista")

        combo_box.move(10, 180)
        self.lbl_style_choice.move(10, 150)
        combo_box.activated[str].connect(self.style_choice)

        cal = QCalendarWidget(self)
        cal.move(200, 200)
        cal.resize(320, 200)

        self.show()

    def color_choice(self):
        color = QColorDialog.getColor()
        self.lbl_style_choice.setStyleSheet("QWidget { background-color: %s}" % color.name())

    def font_choice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.lbl_style_choice.setFont(font)

    def style_choice(self, text):
        self.lbl_style_choice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    def close_application(self):
        choice = QMessageBox.question(self, "Quit!", "You Want Quit The Application?", QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Ok! Good Bye!")
            sys.exit()
        else:
            pass

    def enlarge_window(self, state):
        if state == Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

    def closeEvent(self, event):
        event.ignore()
        self.close_application()


def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
