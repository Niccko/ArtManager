from numpy import source
from folder_hashing import folder_hashing
from utils import *
import os, shutil

class image_loader:
    source_dir = ""
    target_dir = ""
    def __init__(self, target_dir) -> None:
        self.target_dir = target_dir
        self.hashing = folder_hashing(self.target_dir)
        self.hashing.load_hashes()
    
    def check_source(self, source_dir):
        return self.hashing.find_collisions(source_dir)
    
    def load(self, source_dir, remove_dups = False, remove_source = False):
        files = list_subdir(source_dir)
        for file in files:
            filename = os.path.relpath(file, source_dir)
            target_file = os.path.join(self.target_dir, filename)
            if os.path.exists(target_file):
                target_file =  "n_" + target_file
            shutil.copyfile(file, target_file)
        self.hashing.invalidate_hashes()

        
if __name__ == "__main__":
    loader = image_loader("C:\\Users\\radko\Desktop\\target")
    loader.load("C:\\Users\\radko\Desktop\\source")