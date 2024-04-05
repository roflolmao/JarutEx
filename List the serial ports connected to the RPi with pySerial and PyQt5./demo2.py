# -*- coding: UTF-8 -*-
import glob
import serial
from PyQt5.QtWidgets import QApplication, QLabel, QComboBox, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon, QColor
 
class MyApp(QWidget):
    def __init__(self, title, w=640, h=480):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(0, 0, w, h)
        self.status = False

        self.lbl = QLabel("รายการพอร์ตอนุกรม", self)
        self.lbl.move( 100, 20 )
        self.lbl.adjustSize()

        self.cbb = QComboBox(self)
        self.cbb.move( 280, 20 )
        
        ## serial port
        ports = glob.glob('/dev/tty[A-Za-z]*')
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                self.cbb.addItem(port)
            except (OSError, serial.SerialException):
                pass

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyApp("PyQt5 Serial")
    sys.exit(app.exec_())
