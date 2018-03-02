#!/usr/bin/env python

import os
import AppKit
from PyQt5 import QtGui
from PyQt5 import QtWidgets

ContentsDir = os.environ.get("ContentsDir")

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtWidgets.QMenu(parent)

        # Add a test option to the dropdown menu
        testAction = QtWidgets.QAction("TestAction", self, triggered=self.test)
        menu.addAction(testAction)

        menu.addSeparator()

        # Add a quit option to the dropdown menu
        quitAction = QtWidgets.QAction("&Quit", self, triggered=app.quit)
        menu.addAction(quitAction)

        self.setContextMenu(menu)

    def test(self, *args):
        print("test: %s" % (args,))

# Hide the Dock icon, the Alt-tab icon, and the Applciation menu
info = AppKit.NSBundle.mainBundle().infoDictionary()
info["LSBackgroundOnly"] = "1"


app = QtWidgets.QApplication([])

# Configure the MenuBar icon to be a Mask, overlaid against whatever
# color the MenuBar happens to be
icon_file = os.path.join(ContentsDir, "Resources", "BauxTemplate.png")
icon = QtGui.QIcon(icon_file)
icon.setIsMask(True)

trayIcon = SystemTrayIcon(icon)
trayIcon.show()
app.exec_()
