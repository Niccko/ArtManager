from enum import Enum
from typing import Dict, Optional, List
from dataclasses import dataclass, field


class ElementType(Enum):
    image = 1
    video = 2
    library = 3
    unknown = 4


@dataclass
class Element:
    name: Optional[str] = ""
    type: Optional[ElementType] = ElementType.unknown
    path: Optional[str] = ""
    tags: Optional[Dict[str, str]] = field(default_factory=dict)
    res: tuple = (0, 0)


@dataclass
class UiElement:
    obj: Element
    checked: bool
