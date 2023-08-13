from dto import Element, ElementType

from utils import *
from environment import LIB_META_NAME

from PIL import Image
import pickle


def load_element(path) -> Element:
    elem = Element()
    if is_image(path):
        elem.type = ElementType.image
        try:
            im = Image.open(path)
            elem.res = im.size
            im.resize((1, 1))
        except Exception as e:
            print(path)
            elem.type = ElementType.unknown
            print(e)
    elif is_video(path):
        elem.type = ElementType.video
    elif os.path.isdir(path):
        if file_in_folder(path, LIB_META_NAME):
            elem.type = ElementType.library
            lib_info = load_pickle(os.path.join(path, LIB_META_NAME))
            elem.tags = lib_info.get("tags")
    elem.name = os.path.basename(path)
    elem.path = path

    return elem


def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


def save_pickle(path, obj):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)
