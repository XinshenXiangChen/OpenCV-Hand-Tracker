from enum import Enum, auto


class RightHandAction(Enum):
    PAINT = auto()
    ERASE = auto()


class LeftHandAction(Enum):
    ZOOMIN = auto()
    ZOOMOUT = auto()
