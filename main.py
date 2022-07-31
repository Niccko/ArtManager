from utilities.grouping import date_group
from utilities.file_loader import file_loader

if __name__ == "__main__":
    loader = file_loader("C:\\Users\\radko\\Desktop\\test_target")
    loader.load("C:\\Users\\radko\\Desktop\\test_source", remove_dups=True)