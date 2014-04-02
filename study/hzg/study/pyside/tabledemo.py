# -*- coding: utf-8 -*-
import sys

from PySide.QtCore import QAbstractTableModel, Qt
from PySide.QtGui import QApplication, QTableView, QWidget, QVBoxLayout, \
    QAbstractItemView, QSortFilterProxyModel


class Card:
    def __init__(self, name, skill, cost, attack, life):
        self.name = name
        self.skill = skill
        self.cost = cost
        self.attack = attack
        self.life = life
    def __str__(self):
        return self.name

class CardModel(QAbstractTableModel):
    def __init__(self, cards):
        QAbstractTableModel.__init__(self)
        self.cards = cards
        self.fields = ['name', 'skill', 'cost', 'attack', 'life']
        self.headers = [u'名称', u'技能', u'法力', u'攻击', u'血量']
    def rowCount(self, *args, **kwargs):
        return len(self.cards)
    def columnCount(self, *args, **kwargs):
        return 5
    def data(self, idx, role):
        if not idx.isValid():
            return None
        if role == Qt.TextAlignmentRole:
            return Qt.AlignLeft and Qt.AlignVCenter
        if role == Qt.DisplayRole:
            return eval('self.cards[idx.row()].%s' % self.fields[idx.column()])
    def headerData(self, col, orientation, role):
        if  orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[col]
    def flags(self, idx):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable
    
class MainWindow(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        self.resize(640, 480)
        vbox = QVBoxLayout()
        self.setWindowTitle('TableDemo')
        self.setLayout(vbox)
        self.table = QTableView()
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        cards = [Card(u'巫医', u'战吼：恢复2点生命值。', 1, 2, 1), 
                 Card(u'狼骑兵', u'冲锋', 3, 3, 1),
                 Card(u'石牙野猪', u'冲锋', 1, 1, 1),
                 Card(u'森金持盾卫士', u'嘲讽', 4, 3, 5),
                ]
        cardModel = CardModel(cards)
        sortModel = QSortFilterProxyModel()
        sortModel.setSourceModel(cardModel)
        self.table.setModel(sortModel)
        vbox.addWidget(self.table)
        
    def printItem(self, idx):
        print idx.model().persons[idx.row()]

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())

