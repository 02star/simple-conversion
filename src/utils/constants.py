#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    constants.py
# @Author:      周立兵
# @CreationTime:2025/3/4 20:30
# @Description: the script is used to do something.
class FileTypes:
    # 原有文件类型过滤器定义
    PDF = "PDF Files (*.pdf)"
    WORD = "Word Files (*.docx)"
    EXCEL = "Excel Files (*.xlsx)"
    IMAGE = "Image Files (*.png *.jpg *.jpeg)"


class StatusMessages:
    SUCCESS = ("操作成功", 5000)
    FAILURE = ("操作失败", 5000)