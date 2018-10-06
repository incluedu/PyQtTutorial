import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(10, 50, 500, 300)
window.setWindowTitle("PyQt Tuts!")
window.show()

sys.exit(app.exec_())
