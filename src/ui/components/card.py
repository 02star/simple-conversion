#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    card.py
# @Author:      周立兵
# @CreationTime:2025/2/18 20:49
# @Description: the script is used to do something.
from PyQt6.QtCore import QRectF, Qt, pyqtSignal
from PyQt6.QtGui import QPixmap, QPainter, QPainterPath, QColor, QBrush, QPen
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGraphicsDropShadowEffect


class CardWidget(QWidget):
    clicked = pyqtSignal()
    def __init__(self, icon_paths, text):
        super().__init__()
        self.icon_paths = icon_paths
        self.text = text
        self.init_ui()


    def init_ui(self):
        main_layout = QVBoxLayout(self)
        icon_layout = QHBoxLayout()
        for path in self.icon_paths:
            pixmap = QPixmap(str(path))
            label = QLabel(self)
            scaled_pixmap = pixmap.scaled(
                20, 20,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            label.setPixmap(scaled_pixmap)
            icon_layout.addWidget(label)

        # 文本标签
        text_label = QLabel(self.text)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(icon_layout)
        main_layout.addWidget(text_label)
        self.setFixedSize(100, 100)
        self.setLayout(main_layout)

    def enterEvent(self, event):
        super().enterEvent(event)
        self._setup_shadow()

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.setGraphicsEffect(None)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.clicked.emit()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)


        margin = 5
        rect = QRectF(margin, margin, self.width() - 2 * margin, self.height() - 2 * margin)

        path = QPainterPath()
        path.addRoundedRect(rect, 10, 10)

        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.setPen(QPen(QColor(200, 200, 200), 1))
        painter.drawPath(path)

    def _setup_shadow(self):
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor(0, 0, 0, 80))
        shadow.setOffset(3, 3)
        shadow.setBlurRadius(15)
        self.setGraphicsEffect(shadow)
