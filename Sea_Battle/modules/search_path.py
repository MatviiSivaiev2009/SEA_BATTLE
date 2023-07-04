import os

def find_path(name_file):
    find_path = __file__.split("\\")
    del find_path [-1]
    del find_path [-1]
    find_path = "\\".join(find_path)
    find_path = os.path.join(find_path, name_file)
    return find_path