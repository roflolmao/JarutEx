# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon, QColor
 
class MyApp(QWidget):
    def __init__(self, title, w=640, h=480):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(0, 0, w, h)
        self.status = False

        self.my_button = QPushButton("Click-->Yellow::คลิกเพื่อเปลี่ยนเป็นสีเหลือง", self)
        self.my_button.setToolTip("เจอปุ่มก็ต้องกดสินะ!")
        self.my_button.move( 100, 100 )
        self.my_button.clicked[bool].connect(self.on_clicked_my_button)

        self.show()

    def on_clicked_my_button(self):
        source = self.sender()
        if self.status == False:
            self.status = True
            self.setStyleSheet("background-color:yellow;")
            self.my_button.setText("Click-->White::คลิกเพื่อเปลี่ยนเป็นสีขาว")
        else:
            self.status = False
            self.setStyleSheet("background-color:white;")
            self.my_button.setText("Click-->Yellow::คลิกเพื่อเปลี่ยนเป็นสีเหลือง")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyApp("PyQt5: สวัสดีคิวท์5  มีปุ่มกด ก็ต้องกดปุ่ม")
    sys.exit(app.exec_())
