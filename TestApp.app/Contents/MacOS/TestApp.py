#!/usr/bin/env python

from PyQt5 import QtGui
from PyQt5 import QtWidgets

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtWidgets.QMenu(parent)
        testAction = QtWidgets.QAction("TestAction", self, triggered=self.test)
        menu.addAction(testAction)
        self.setContextMenu(menu)

    def test(self, *args):
        print("test: %s" % (args,))

app = QtWidgets.QApplication([])
icon = QtGui.QIcon(
           app.style().standardPixmap(
               QtWidgets.QStyle.SP_DirIcon
           )
       )
trayIcon = SystemTrayIcon(icon)
trayIcon.show()
app.exec_()
