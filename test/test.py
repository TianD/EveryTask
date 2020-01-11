#!/usr/bin/env python
# coding=utf-8
# Copyright (c) 2019 MoreVFX. All rights reserved.
# created by huiguoyu @ 2019/11/28 11:47


import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)