#!/usr/bin/env python
# coding=utf-8
# Copyright (c) 2019 MoreVFX. All rights reserved.
# created by huiguoyu @ 2019/11/15 15:11

import os
import sys
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui

from env import SRC_DIR


class Tray(QtWidgets.QSystemTrayIcon):

    def __init__(self, parent=None):
        super(Tray, self).__init__(parent)

        self.setupUi(self)
        # self.setupMenu()
        # self.setupProcessor()

    def setupUi(self, parent):
        # 设置UI
        self.setIcon(QtGui.QIcon(os.path.join(SRC_DIR, 'icon/task.png')))
        self.context_menu = QtWidgets.QMenu()
        self.setContextMenu(self.context_menu)
        self.context_menu.addAction(QtWidgets.QAction('close'))

    # def setupProcessor(self):
    #     # 设置进程
    #     app = QtWidgets.QApplication.instance()
    #     a = StreamlitSlider()
    #     a.show()
    #     app.exec_()