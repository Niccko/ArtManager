from .folder_hashing import folder_hashing
from environment import *
from utilities.grouping.date_grouper import date_group
from utils import *
import os, shutil


class file_loader:
    target_dir = ""

    def __init__(self, target_dir) -> None:
        self.target_dir = target_dir
        self.hashing = folder_hashing(self.target_dir)

    def check_source(self, source_dir):
        return self.hashing.find_collisions(source_dir)

    def load(self, source_dir, remove_dups=False, remove_source=False):
        grouper = date_group()

        files = list_subdir(source_dir)
        dups = []
        if os.path.exists(os.path.join(self.target_dir, TMP_LOADER_DIR_NAME)):
            shutil.rmtree(os.path.join(self.target_dir, TMP_LOADER_DIR_NAME))
        os.makedirs(os.path.join(self.target_dir, TMP_LOADER_DIR_NAME))
        for file in files:
            filename = os.path.basename(file)
            tmp_file = os.path.join(self.target_dir, TMP_LOADER_DIR_NAME, filename)
            if tmp_file in dups:
                continue
            shutil.move(file, tmp_file)

        grouper.execute(os.path.join(self.target_dir, TMP_LOADER_DIR_NAME), target=self.target_dir)
        shutil.rmtree(os.path.join(self.target_dir, TMP_LOADER_DIR_NAME))
