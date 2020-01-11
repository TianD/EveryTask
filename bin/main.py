#!/usr/bin/env python
# coding=utf-8
# Copyright (c) 2019 MoreVFX. All rights reserved.
# created by huiguoyu @ 2019/11/15 17:42

import sys

from PySide2 import QtWidgets

import env

from tray.Tray import Tray


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tray = Tray()
    tray.show()
    app.exec_()