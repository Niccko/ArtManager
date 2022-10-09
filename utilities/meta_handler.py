from enum import Enum
from dataclasses import dataclass, field
from utils import *
from environment import LIB_META_NAME
from typing import Dict, Optional
import pickle

class ElementType(Enum):
    image = 1
    library = 2

@dataclass
class element:
    name: Optional[str] = ""
    type: Optional[ElementType] = ElementType.image
    path: Optional[str] = ""
    tags: Optional[Dict[str, str]] = field(default_factory=dict)



def loadElement(path) -> element:
        elem = element(type = ElementType.image)
        if os.path.isdir(path):
            if file_in_folder(path, LIB_META_NAME):
                elem.type = ElementType.library
                lib_info = loadPickle(os.path.join(path, LIB_META_NAME))
                elem.tags = lib_info.get("tags")
        elem.name = os.path.basename(path)
        elem.path = path
        return elem 

def loadPickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)
        

def savePickle(path, obj):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)
        

