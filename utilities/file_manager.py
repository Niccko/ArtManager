from dataclasses import dataclass
import os, pickle

class file_manager:
    def __init__():
        pass

    def read_meta(path):
        pass

    

    def generate_meta(dir_props):
        for path in dir_props:
            if os.path.isdir(path):
                element = element()
                element.is_folder = os.path.isdir(path)
                element.is_comix = dir_props[path] == "comix"
                element.type = os.path.splitext(path)[1]
                if element.type == "": element.type = "dir"
                element.path = path
            if element.type == "dir":
                with(os.path.join(element.path, "_meta.pkl")) as p:
                    bin = pickle.dumps(element)
                    p.write(bin)
        


    

@dataclass
class element:
    is_folder: bool
    is_comix: bool
    type: str
    path: str
    tags: list[str]

print(os.path.splitext("path")[1])
