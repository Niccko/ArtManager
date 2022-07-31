import os
from datetime import date, datetime as dt
from pprint import pprint
from environment import PARTITION_PREFIX
from shutil import move

import utils

class date_group:
    def __init__(self, path, target = None, affect_folders = False) -> None:
        self.path = path
        self.affect_folders = affect_folders
        self.dates = {}
        self.target = target
        if not target:
            self.target = path

    def execute(self):
        self._group(self.path)

    def _group(self, path = None):
        files = os.listdir(path)
        for file in files:
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path) and self.affect_folders:
                print(f"Grouping folder {file_path}")
                self._group(file_path)
                #TODO Сделать расфасовку папок
                pass
            elif os.path.isfile(file_path):
                unix_date = os.path.getmtime(file_path)
                date = dt.utcfromtimestamp(unix_date).strftime('%Y-%m')
                if not self.dates.get(date):
                    self.dates[date] = 1
                    dir_path = os.path.join(self.target, PARTITION_PREFIX+date)
                    if not os.path.exists(dir_path):
                        os.makedirs(dir_path)
                else:
                    self.dates[date] += 1
                move(file_path, os.path.join(self.target, PARTITION_PREFIX+date, utils.uniquify_filename(file)))


