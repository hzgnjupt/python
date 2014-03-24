# -*- coding: utf-8 -*-
import sys
from PySide.QtGui import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel('<font size=20 color=red>Hello<br/>World</font>')
label.show()
app.exec_()
