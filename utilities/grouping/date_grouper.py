import os
from datetime import date, datetime as dt
from pprint import pprint
from environment import PARTITION_PREFIX
from shutil import move

import utils

class date_group:
    def __init__(self) -> None:
        pass

    def execute(self, path, target = None, affect_partitions = False, affect_folders = False):
        self._group(path, target, affect_partitions, affect_folders)

    def _group(self, path, target = None, affect_partitions = False,affect_folders = False):
        elements = os.listdir(path)
        if not target:
            target = path

        for elem in elements:
            elem_path = os.path.join(path, elem)
            if os.path.isdir(elem_path):
                is_partition = elem.startswith(PARTITION_PREFIX)
                if affect_partitions and is_partition or affect_folders and not is_partition:
                    self._group(elem_path, target)
                
            elif os.path.isfile(elem_path):
                unix_date = os.path.getmtime(elem_path)
                date = dt.utcfromtimestamp(unix_date).strftime('%Y-%m')
                dir_path = os.path.join(target, date)
                if not  os.path.exists(dir_path):
                    os.makedirs(dir_path)
                elem_target = os.path.join(target, date, elem)
                elem_target = utils.uniquify_filename(elem_target)
                move(elem_path, elem_target)

