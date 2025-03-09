#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    path_manager.py
# @Author:      周立兵
# @CreationTime:2025/2/19 22:24
# @Description: the script is used to do something.
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar, Final


@dataclass(frozen=True, slots=True)  # 冻结实例保障线程安全，slots优化内存
class IconPaths:
    """图标路径统一管理类"""
    _BASE_DIR: ClassVar[Path] = Path(__file__).resolve().parent.parent.parent / "assets" / "icons"

    PDF: Final[Path] = _BASE_DIR / "pdf.png"
    WORD: Final[Path] = _BASE_DIR / "word.png"
    ARROW: Final[Path] = _BASE_DIR / "right_arrow.png"
    IMAGE: Final[Path] = _BASE_DIR / "image.png"
    EXCEL: Final[Path] = _BASE_DIR / "excel.png"

    def __post_init__(self) -> None:
        """初始化时验证路径是否存在"""
        for name, path in self.__dict__.items():
            if not path.exists():
                raise FileNotFoundError(f"图标资源缺失: {name} -> {path}")


# 单例模式实例化（线程安全）
Icons = IconPaths()
