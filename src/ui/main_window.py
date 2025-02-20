#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    main_window.py
# @Author:      周立兵
# @CreationTime:2025/2/19 22:06
# @Description: the script is used to do something.
import os
import sys

import pymupdf
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QFileDialog, QWidget, QMessageBox
from pdf2docx import parse

from src.ui.base_window import BaseWindow

from src.ui.components.card import CardWidget
from src.ui.components.flow_layout import FlowLayout
from src.utils.path_manager import PDF_ICON, RIGHT_ARROW_ICON, WORD_ICON, IMAGE_ICON


class MainWindow(BaseWindow):

    def __init__(self):
        super().__init__()
        self.second_window = None
        self.init_ui()

    def init_ui(self):
        container = QWidget()
        layout = FlowLayout(container)
        card1 = CardWidget([PDF_ICON,RIGHT_ARROW_ICON,WORD_ICON],'PDF转WORD')
        card1.clicked.connect(self.pdf_to_word)
        layout.addWidget(card1)

        card2 = CardWidget([PDF_ICON, RIGHT_ARROW_ICON, IMAGE_ICON], 'PDF转IMAGE')
        card2.clicked.connect(self.pdf_to_image)
        layout.addWidget(card2)

        self.setCentralWidget(container)
        self.resize(300, 200)


    def pdf_to_word(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择PDF文件",
            "",
            "PDF Files (*.pdf)"
        )
        if not file_path:
            return
        file_name = os.path.basename(file_path)
        output_path, _ = QFileDialog.getSaveFileName(
            self,
            "保存Word文件",
            file_name,
            "Word Files (*.docx)"
        )
        if not output_path:
            return
        if file_path:
            try:
                parse(file_path, output_path)
                self.statusBar().showMessage('转换完成',5000)
            except Exception as e:
                QMessageBox.critical(self, "错误", f"转换失败：{str(e)}")
                self.statusBar().showMessage('转换失败',5000)

    def pdf_to_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择PDF文件",
            "",
            "PDF Files (*.pdf)"
        )

        if file_path:
            save_dir = QFileDialog.getExistingDirectory(self, "选择保存目录")
            try:
                with pymupdf.open(file_path) as pdf:
                    for page in pdf:
                        pix = page.get_pixmap()
                        pix.save(save_dir+"/"+os.path.basename(file_path)+f"-{page.number}.png")
                self.statusBar().showMessage('转换完成',5000)
            except Exception as e:
                QMessageBox.critical(self, "错误", f"转换失败：{str(e)}")
                self.statusBar().showMessage('转换失败',5000)


def main_window():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../../assets/icon.png'))
    main = MainWindow()
    main.show()
    sys.exit(app.exec())