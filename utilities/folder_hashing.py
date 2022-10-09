from utils import *
import pickle
import os
from environment import HASHES_FILE_NAME
from utilities.meta_handler import *


class folder_hashing:
    def __init__(self, path = None) -> None:
        self.path = path
        self.hashes = {}
        self.files = []
    
    def invalidate_hashes(self, rescan = False, path = None):
        self.path = path if path else self.path
        if not self.path:
            raise Exception("Observable path is not specified.")
        existing = list(map(lambda f: f.path, sum(self.hashes.values(), [])))
        files = list_subdir(self.path)
        for i, x in enumerate(files):
            fileElem = loadElement(x)
            if fileElem.type == ElementType.image:
                if x not in existing:
                    hash = compute_hash(x)
                    if not hash in self.hashes:
                        self.hashes[hash] = []
                    self.hashes[hash].append(fileElem)
                
        self.save_hashes(os.path.join(self.path, HASHES_FILE_NAME))
    
    def save_hashes(self, path):
        savePickle(path, self.hashes)

    def load_hashes(self, path = None):
        filepath = os.path.join(self.path, HASHES_FILE_NAME)
        if os.path.exists(filepath):
            self.hashes = loadPickle(filepath)
        else:
            self.invalidate_hashes()

    def find_image(self, img_path, force_load = False):
        img_hash = compute_hash(img_path)
        if force_load or not self.hashes:
            self.load_hashes(self.path)
        return self.hashes.get(img_hash)

    def find_duplicates(self):
        return list(filter(lambda x: len(x)>1, list(self.hashes.values())))

    def find_collisions(self, source = None):
        collisions = []
        files = map(lambda x: os.path.join(source, x), os.listdir(source))
        for file in files:
            if is_image(file):
                compare = self.find_image(file)
                if compare:
                    collisions.append({
                        "target": compare,
                        "source": file
                    })
        return collisions
