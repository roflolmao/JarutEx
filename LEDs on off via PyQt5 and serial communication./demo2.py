# -*- coding: UTF-8 -*-
import sys
import glob
import serial
from PyQt5.QtWidgets import QApplication, QCheckBox, QLabel, QComboBox, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon, QColor

class MyApp(QMainWindow):
    def __init__(self, title, w=640, h=480):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(0, 0, w, h)
        self.status = False

        self.lbl = QLabel("รายการพอร์ตอนุกรม", self)
        self.lbl.move( 100, 20 )
        self.lbl.adjustSize()

        self.lbl2 = QLabel("สถานะ", self)
        self.lbl2.move( 100, 70)
        self.lbl2.adjustSize()

        self.cbb = QComboBox(self)
        self.cbb.move( 220, 20 )

        ## serial port
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(128)]
        elif sys.platform.startswith('linux'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/cu.*')
        else:
            raise EnvironmentError('ไม่รองรับการทำงานของระบบปฏิบัติการนี้!!!')
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                self.cbb.addItem(port)
            except (OSError, serial.SerialException):
                pass
        self.cbb.adjustSize()

        ### Check box
        self.chkLeds = []
        for i in range(8):
            self.chkLeds.append(QCheckBox("LED{}".format(i),self))
            self.chkLeds[i].move(100+(i*64),110)

        ### send button
        self.btnSend = QPushButton("ส่งข้อมูล", self)
        self.btnSend.setToolTip("ส่งข้อมูลไปที่พอร์ตอนุกรม")
        self.btnSend.move( 200, 68 )
        self.btnSend.clicked[bool].connect(self.on_clicked_btnSend)

        ## status bar
        if self.cbb.count() > 0:
            self.statusBar().showMessage('status: พร้อมทำงาน')
        else:
            self.statusBar().showMessage('status: ไม่พบพอร์ตอนุกรม')
        self.show()


    def on_clicked_btnSend(self):
        source = self.sender()
        #print(self.cbb.count(), self.cbb.currentText())
        if (self.cbb.count() == 0):
          return
        ### แปลงข้อมูล
        data = 0
        if (self.chkLeds[0].isChecked()):
          data += 1
        if (self.chkLeds[1].isChecked()):
          data += 2
        if (self.chkLeds[2].isChecked()):
          data += 4
        if (self.chkLeds[3].isChecked()):
          data += 8
        if (self.chkLeds[4].isChecked()):
          data += 16
        if (self.chkLeds[5].isChecked()):
          data += 32
        if (self.chkLeds[6].isChecked()):
          data += 64
        if (self.chkLeds[7].isChecked()):
          data += 128
        data = "{}\n".format(data)
        encoded_string = data.encode()
        byte_array = bytearray(encoded_string)
        print(byte_array)
        port = self.cbb.currentText()
        try:
          scon = serial.Serial(port=port,baudrate=115200)
          scon.write(byte_array)
          scon.flushOutput()
          scon.close()
        except:
          self.statusBar().showMessage("{} เปิดใช้ไม่ได้!!!".format(port))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyApp("PyQt5 serial 3",640, 320)
    sys.exit(app.exec_())
