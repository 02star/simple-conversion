#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    main_window.py
# @Author:      周立兵
# @CreationTime:2025/2/19 22:06
# @Description: the script is used to do something.
import os
import sys
from functools import wraps
from typing import Tuple

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QFileDialog, QWidget, QMessageBox

from src.core.img_converter import ImageConverter
from src.core.pdf_converter import PDFConverter
from src.core.word_converter import WordConverter
from src.ui.base_window import BaseWindow
from src.ui.components.card import CardWidget
from src.ui.components.flow_layout import FlowLayout
from src.utils.constants import FileTypes
from src.utils.path_manager import Icons


def _get_input_path(parent: QWidget,title: str,default_name: str,file_filter: str) -> Tuple[str, str]:
    return QFileDialog.getOpenFileName(parent, title, default_name, file_filter)

def _get_output_path(parent: QWidget,title: str,default_name: str,file_filter: str) -> Tuple[str, str]:
    return QFileDialog.getSaveFileName(parent, title, default_name, file_filter)

def _get_output_dir(parent: QWidget, title: str) -> str:
    return QFileDialog.getExistingDirectory(parent, title)


def handle_conversion(input_type: str, output_type: str, output_mode: str = "file"):
    def decorator(process_func):
        @wraps(process_func)
        def wrapper(self):
            # 统一处理文件选择逻辑
            input_path, _ = _get_input_path(self, "选择文件", "", input_type)
            if not input_path:
                return

            # 统一处理输出路径逻辑
            if output_mode == "directory":
                output_path = _get_output_dir(self, "选择保存目录")
            else:
                file_name = os.path.splitext(input_path)[0]
                output_path, _ = _get_output_path(self, "保存文件", file_name, output_type)

            if not output_path:
                return

            # 统一处理异常捕获和状态更新
            try:
                process_func(self, input_path, output_path)
                self.statusBar().showMessage('转换完成', 5000)
            except Exception as e:
                QMessageBox.critical(self, "错误", f"转换失败：{str(e)}")
                self.statusBar().showMessage('转换失败', 5000)

        return wrapper
    return decorator

class MainWindow(BaseWindow):

    def __init__(self):
        super().__init__()
        self.second_window = None
        self.init_ui()

    def init_ui(self):
        container = QWidget()
        layout = FlowLayout(container)

        cards = [
            ([Icons.PDF, Icons.ARROW, Icons.WORD],"PDF转WORD",self.pdf_to_word),
            ([Icons.PDF, Icons.ARROW, Icons.IMAGE],"PDF转图片",self.pdf_to_image),
            ([Icons.IMAGE, Icons.ARROW, Icons.EXCEL],"图片转Excel",self.img_to_excel),
            ([Icons.WORD, Icons.ARROW, Icons.PDF],"Word转PDF",self.word_to_pdf)
        ]
        for icons, title, callback in cards:
            card = CardWidget(icons, title)
            card.clicked.connect(callback)
            layout.addWidget(card)

        self.setCentralWidget(container)
        self.resize(600, 400)

    @handle_conversion(input_type=FileTypes.PDF,output_type=FileTypes.WORD)
    def pdf_to_word(self, input_path, output_path):
        PDFConverter.to_word(input_path, output_path)

    @handle_conversion(input_type=FileTypes.PDF,output_type=FileTypes.IMAGE,output_mode="directory")
    def pdf_to_image(self, input_path, output_path):
        PDFConverter.to_img(input_path, output_path)

    @handle_conversion(input_type=FileTypes.IMAGE,output_type=FileTypes.EXCEL)
    def img_to_excel(self, input_path, output_path):
        ImageConverter.image_to_excel(input_path, output_path)

    @handle_conversion(input_type=FileTypes.WORD,output_type=FileTypes.PDF)
    def word_to_pdf(self, input_path, output_path):
        WordConverter.word_to_pdf(input_path, output_path)


def main_window():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r'C:\Workspaces\simple-conversion\assets\icon.png'))
    main = MainWindow()
    main.show()
    sys.exit(app.exec())