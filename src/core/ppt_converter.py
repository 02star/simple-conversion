#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    ppt_converter.py
# @Author:      周立兵
# @CreationTime:2025/3/11 11:51
# @Description: the script is used to do something.
from win32com import client


class PPTConverter:
    @staticmethod
    def to_pdf(input_path, output_path):
        powerpoint = client.Dispatch("PowerPoint.Application")
        powerpoint.Visible = 0
        with powerpoint.Presentations.Open(input_path) as ppt:
            ppt.SaveAs(output_path, 17)