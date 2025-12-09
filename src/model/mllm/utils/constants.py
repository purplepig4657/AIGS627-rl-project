
from enum import Enum, unique
from typing import Optional
from src.utils.constants import add_enum_utilities



@unique
@add_enum_utilities
class LoadMode(Enum):
    LOCAL:  str = "local"
    REMOTE: str = "remote"