#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    assets.py
# @Author:      周立兵
# @Created:     2025/2/19
# @Description: 应用资源路径
from dataclasses import dataclass, fields
from pathlib import Path
from typing import ClassVar, Final


@dataclass(frozen=True)
class IconAssets:

    _PROJECT_ROOT: ClassVar[Path] = Path(__file__).resolve().parent.parent.parent
    _DEFAULT_ICON_DIR: ClassVar[Path] = _PROJECT_ROOT / "assets" / "icons"


    PDF: Final[Path] = _DEFAULT_ICON_DIR / "pdf.png"
    WORD: Final[Path] = _DEFAULT_ICON_DIR / "word.png"
    ARROW: Final[Path] = _DEFAULT_ICON_DIR / "right_arrow.png"
    IMAGE: Final[Path] = _DEFAULT_ICON_DIR / "image.png"
    EXCEL: Final[Path] = _DEFAULT_ICON_DIR / "excel.png"
    PPT: Final[Path] = _DEFAULT_ICON_DIR / "ppt.png"


    APP_LOGO: Final[Path] = _PROJECT_ROOT / "assets" /  "logo.png"


APP_ICONS: Final[IconAssets] = IconAssets()