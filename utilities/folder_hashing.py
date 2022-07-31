from utils import *
import pickle
import os
from environment import HASHES_FILE_NAME


class folder_hashing:
    def __init__(self, path = None) -> None:
        self.path = path
        self.hashes = {}
    
    def invalidate_hashes(self, rescan = False, path = None):
        self.path = path if path else self.path
        if not self.path:
            raise Exception("Observable path is not specified.")
        files = list_subdir(self.path)
        for i,x in enumerate(files):
            if rescan or x not in self.hashes.values():
                if is_image(x):
                    hash = compute_hash(x)
                    self.hashes[hash] = [x]
        self.save_hashes(os.path.join(self.path, HASHES_FILE_NAME))
    
    def save_hashes(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self.hashes, f)

    def load_hashes(self, path = None):
        filepath = os.path.join(self.path, HASHES_FILE_NAME)
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                self.hashes = pickle.load(f)
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
                        "target": file,
                        "source": compare
                    })
        return collisions
