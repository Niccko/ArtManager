from numpy import source
from .folder_hashing import folder_hashing
from environment import *
from utilities.grouping.date_grouper import date_group
from utils import *
import os, shutil
from pprint import pprint

class file_loader:
    target_dir = ""
    def __init__(self, target_dir) -> None:
        self.target_dir = target_dir
        self.hashing = folder_hashing(self.target_dir)
        self.hashing.load_hashes()
    
    def check_source(self, source_dir):
        return self.hashing.find_collisions(source_dir)
    
    def load(self, source_dir, remove_dups = False, remove_source = False):
        files = list_subdir(source_dir)
        dups = []
        if remove_dups:
            for x in self.hashing.find_collisions(source_dir):
                dups.extend(x["source"])
        if os.path.exists(os.path.join(self.target_dir, TMP_LOADER_DIR_NAME)):
                shutil.rmtree(os.path.join(self.target_dir, TMP_LOADER_DIR_NAME))
        os.makedirs(os.path.join(self.target_dir, TMP_LOADER_DIR_NAME))
        for file in files:      
            filename = os.path.relpath(file, source_dir)
            tmp_file = os.path.join(self.target_dir, TMP_LOADER_DIR_NAME, filename)
            if tmp_file in dups:
                continue  
            shutil.move(file, tmp_file)
        grouper = date_group(os.path.join(self.target_dir, TMP_LOADER_DIR_NAME), target=self.target_dir)
        grouper.execute()
        shutil.rmtree(os.path.join(self.target_dir, TMP_LOADER_DIR_NAME))
        #self.hashing.invalidate_hashes()


        
