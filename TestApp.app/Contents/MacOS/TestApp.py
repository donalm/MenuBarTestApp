#!/usr/bin/env python

import AppKit
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

info = AppKit.NSBundle.mainBundle().infoDictionary()
info["LSBackgroundOnly"] = "1"

app = QtWidgets.QApplication([])
icon = QtGui.QIcon(
           app.style().standardPixmap(
               QtWidgets.QStyle.SP_DirIcon
           )
       )
trayIcon = SystemTrayIcon(icon)
trayIcon.show()
app.exec_()
