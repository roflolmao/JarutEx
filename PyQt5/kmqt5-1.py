#kmqt5-1.py
# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
 
class MyApp(QWidget):
 
    def __init__(self, title, w, h):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(0, 0, w, h)
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyApp("PyQt5: สวัสดีคิวท์5", 640, 480)
    sys.exit(app.exec_())
