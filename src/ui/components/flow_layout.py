#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    flow_layout.py
# @Author:      周立兵
# @CreationTime:2025/2/18 22:45
# @Description: the script is used to do something.
from PyQt6.QtWidgets import QLayout, QWidgetItem, QLayoutItem, QSizePolicy
from PyQt6.QtCore import QRect, QSize, Qt


class FlowLayout(QLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.itemList = []

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        return self.itemList[index] if 0 <= index < len(self.itemList) else None

    def takeAt(self, index):
        return self.itemList.pop(index) if 0 <= index < len(self.itemList) else None

    def setGeometry(self, rect):
        super().setGeometry(rect)
        self._do_layout(rect, apply_geometry=True)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()
        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())
        return size

    def _do_layout(self, rect, apply_geometry=False):
        x = rect.x()
        y = rect.y()
        line_height = 0

        for item in self.itemList:
            widget = item.widget()
            space_x = self.spacing() + widget.style().layoutSpacing(
                QSizePolicy.ControlType.PushButton,
                QSizePolicy.ControlType.PushButton,
                Qt.Orientation.Horizontal
            )
            space_y = self.spacing() + widget.style().layoutSpacing(
                QSizePolicy.ControlType.PushButton,
                QSizePolicy.ControlType.PushButton,
                Qt.Orientation.Vertical
            )

            next_x = x + item.sizeHint().width() + space_x
            if next_x - space_x > rect.right() and line_height > 0:
                x = rect.x()
                y = y + line_height + space_y
                next_x = x + item.sizeHint().width() + space_x
                line_height = 0

            if apply_geometry:
                item.setGeometry(QRect(x, y, item.sizeHint().width(), item.sizeHint().height()))

            x = next_x
            line_height = max(line_height, item.sizeHint().height())

        return QSize(rect.width(), y + line_height - rect.y())
