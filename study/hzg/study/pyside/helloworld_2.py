# -*- coding: utf-8 -*-
import sys
from PySide.QtGui import QApplication
from PySide.QtDeclarative import QDeclarativeView
from PySide.QtCore import QUrl

app = QApplication(sys.argv)
view = QDeclarativeView()
view.setSource(QUrl('helloworld_2.qml'))
view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
view.show()
app.exec_()
