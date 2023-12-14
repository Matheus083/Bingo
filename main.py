from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QMainWindow, QWidget
from base import MaskLayout
import os
import sys

os.system('clear')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    center_widget = QWidget()
    t = MaskLayout()
    t.configMask()
    b = QPushButton('Button')
    b.setStyleSheet('font-size: 40px')
    b.show()
    center_widget.setLayout(t)
    app.exec()
