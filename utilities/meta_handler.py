from enum import Enum
from dataclasses import dataclass, field
from utils import *
from environment import LIB_META_NAME
from typing import Dict, Optional
from PIL import Image
import pickle

class ElementType(Enum):
    image = 1
    video = 2
    library = 3
    unknown = 4

@dataclass
class element:
    name: Optional[str] = ""
    type: Optional[ElementType] = ElementType.unknown
    path: Optional[str] = ""
    tags: Optional[Dict[str, str]] = field(default_factory=dict)
    res: tuple = (0,0)



def loadElement(path) -> element:
        elem = element()
        if is_image(path):
            elem.type = ElementType.image
            try:
                im = Image.open(path)
                elem.res = im.size
                im.resize((1,1))
            except Exception as e:
                print(path)
                elem.type = ElementType.unknown
                print(e) 
        elif is_video(path):
            elem.type = ElementType.video
        elif os.path.isdir(path):
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
        

