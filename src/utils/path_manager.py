#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    path_manager.py
# @Author:      周立兵
# @CreationTime:2025/2/19 22:24
# @Description: the script is used to do something.
import os

_current_file_path = os.path.abspath(__file__)
_project_root = os.path.dirname(os.path.dirname(os.path.dirname(_current_file_path)))
ASSETS_DIR = os.path.join(_project_root, 'assets\\icons')

PDF_ICON = os.path.join(ASSETS_DIR, 'pdf.png')
WORD_ICON = os.path.join(ASSETS_DIR, 'word.png')
RIGHT_ARROW_ICON = os.path.join(ASSETS_DIR, 'right_arrow.png')
IMAGE_ICON = os.path.join(ASSETS_DIR, 'image.png')