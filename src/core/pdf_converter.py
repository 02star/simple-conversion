#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    pdf_converter.py
# @Author:      周立兵
# @CreationTime:2025/2/22 11:14
# @Description: the script is used to do something.
import os

import pandas as pd
import pdfplumber
import pymupdf
from pdf2docx import parse
from tqdm import tqdm


class PDFConverter:

    @staticmethod
    def to_word(input_path, output_path):
        parse(input_path, output_path)

    @staticmethod
    def to_img(input_path, output_path):
        with pymupdf.open(input_path) as pdf:
            for i,page in enumerate(pdf):
                file_name = os.path.join(output_path, f"{os.path.splitext(os.path.basename(input_path))}-{i+1}.png")
                pix = page.get_pixmap()
                pix.save(file_name)

    @staticmethod
    def to_excel(input_path, output_path):
        with pdfplumber.open(input_path) as pdf:
            all_tables = []
            for page in pdf.pages:
                # 提取当前页表格
                tables = page.extract_tables()
                for table in tqdm(tables, desc=f"Processing Page {page.page_number}"):
                    all_tables.extend(table)

            # 转换为DataFrame并保存
            df = pd.DataFrame(all_tables[1:], columns=all_tables[0])
            df.to_excel(output_path, index=False)
