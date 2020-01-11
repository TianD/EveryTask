#!/usr/bin/env python
# coding=utf-8
# Copyright (c) 2019 MoreVFX. All rights reserved.
# created by huiguoyu @ 2019/11/15 18:02

import os
import sys

BIN_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(BIN_DIR)

SRC_DIR = os.path.join(ROOT_DIR, 'src')
PLUGIN_DIR = os.path.join(ROOT_DIR, 'plugins')
LIB_DIR = os.path.join(ROOT_DIR, 'libs')
CONFIG_DIR = os.path.join(ROOT_DIR, 'configs')
SCRIPT_DIR = os.path.join(ROOT_DIR, 'scripts')

sys.path.append(SRC_DIR)
sys.path.append(PLUGIN_DIR)
sys.path.append(LIB_DIR)
sys.path.append(CONFIG_DIR)
sys.path.append(SCRIPT_DIR)
