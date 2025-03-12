#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    excel_converter.py
# @Author:      周立兵
# @CreationTime:2025/3/11 11:30
# @Description: the script is used to do something.
from win32com import client


class ExcelConverter:
    @staticmethod
    def to_pdf(input_path, output_path):
        excel = client.Dispatch("Excel.Application")
        excel.Visible = False  # 不显示界面

        # 打开工作簿
        workbook = excel.Workbooks.Open(input_path)

        # 导出为PDF，Type=0表示PDF格式
        workbook.ExportAsFixedFormat(
            Type=0,  # PDF格式
            Filename=output_path,
            Quality=0,  # 质量标准（0为标准）
            IncludeDocProperties=True,  # 包含文档属性
            IgnorePrintAreas=False,  # 不忽略打印区域
            OpenAfterPublish=False  # 转换后不打开PDF
        )