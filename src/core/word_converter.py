#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    word_converter.py
# @Author:      周立兵
# @CreationTime:2025/3/3 23:10
# @Description: the script is used to do something.
from docx2pdf import convert


class WordConverter:
    @staticmethod
    def to_pdf(input_path, output_path):
        convert(input_path, output_path)