#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    img_converter.py
# @Author:      周立兵
# @CreationTime:2025/2/22 18:59
# @Description: the script is used to do something.
import pytesseract
from PIL import Image
import cv2
from paddleocr import PPStructure, draw_structure_result
import pandas as pd

class ImageConverter:
    @staticmethod
    def image_to_excel(input_path, output_path):
        # 初始化模型
        table_engine = PPStructure(
            show_log=True,
            recovery=True,  # 启用表格结构恢复
            use_gpu=False
        )
        img = cv2.imread(input_path)

        # 执行分析
        result = table_engine(img)

        # 提取表格数据
        tables = []
        for region in result:
            html_str = region['res']['html']
            tables.append(pd.read_html(html_str)[0])


        final_df = pd.concat(tables)
        final_df.to_excel(output_path, index=False)
