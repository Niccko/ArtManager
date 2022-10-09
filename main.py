from pprint import pprint
from utilities.file_loader import file_loader
from utilities.folder_hashing import folder_hashing
import time

if __name__ == "__main__":
    loader = file_loader("D:\\hen")
    loader.load("D:\\hen\\to_load", remove_dups=False)

