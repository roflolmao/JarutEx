#kmqt5-2.py
# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon
 
class MyApp(QMainWindow):
 
    def __init__(self, title, w=640, h=480):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(0, 0, w, h)
        self.statusBar().showMessage('status: สถานะอยู่ตรงนี้!')
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyApp("PyQt5: สวัสดีคิวท์5 มีสเตตัสบาร์แล้วนะ")
    sys.exit(app.exec_())
