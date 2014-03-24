# -*- coding: utf-8 -*-

import sys

from PySide.QtCore import QAbstractListModel, Qt
from PySide.QtGui import QWidget, QApplication, QVBoxLayout, QListView


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return '%s - %s' % (self.name, self.age)

class PersonModel(QAbstractListModel):
    
    def __init__(self, persons):
        QAbstractListModel.__init__(self)
        self.persons = persons
    
    def rowCount(self, idx):
        return len(self.persons)
    
    def data(self, idx, role):
        if role == Qt.DisplayRole:
            return self.persons[idx.row()].name

class MainWindow(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        self.lst = QListView(self)
        self.lst.setModel(PersonModel([Person('HZG', 28), Person('ZRH', 21)]))
        self.lst.clicked.connect(self.printItem)
        vbox.addWidget(self.lst)
        
    def printItem(self, idx):
        print idx.model().persons[idx.row()]
        

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
