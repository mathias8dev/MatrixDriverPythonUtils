import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

def window():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    window()