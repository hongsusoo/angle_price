import sys
from PyQt5.QtWidgets import QWidget, QLCDNumber,QSlider, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
        
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)


        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Signal and slot")
        self.show()
    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Escape:
            self.close()    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())