# -*- coding: utf-8 -*-
import sys

from PySide import QtGui
from PySide.QtGui import QMainWindow, QApplication, QLabel, QGridLayout, \
    QPushButton, QWidget, QMessageBox, QFileDialog
from PySide.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        self.titleCmb = QtGui.QComboBox(self)
        self.titleCmb.addItem('Windows')
        self.titleCmb.addItem('iOS')
        self.titleCmb.addItem('Linux')
        self.titleCmb.addItem('AIX')
        self.titleCmb.activated[str].connect(self.selectTitle)
                
        self.titleEdit = QtGui.QLineEdit()
        self.titleEdit.setDragEnabled(True)
        self.authorEdit = QtGui.QLineEdit()
        self.reviewEdit = QtGui.QTextEdit()
        self.loadButton = QtGui.QPushButton('Load')
        self.loadButton.clicked.connect(self.loadFile)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.setRowStretch(4, 1)
        
        grid.addWidget(self.titleCmb, 0, 1)

        grid.addWidget(title, 1, 0)
        grid.addWidget(self.titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(self.authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(self.reviewEdit, 3, 1, 2, 1)
        
        grid.addWidget(self.loadButton, 5, 1, Qt.AlignRight)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        
    def selectTitle(self, text):
        self.titleEdit.setText(text)
        
    def loadFile(self):
        filename, _ = QFileDialog.getOpenFileName()
        with open(filename) as f:
            self.reviewEdit.setText(f.read())

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()

print 'finish'
