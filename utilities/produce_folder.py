import os


def make_folder(path_folder:str) -> None:
    """
    Create folder if required
    """
    os.path.exists(path_folder) or os.mkdir(path_folder)

def check_presence_folder(path_folder:str) -> bool:
    """
    Check that folder is present
    """
    os.path.exists(path_folder) and os.path.isdir(path_folder)

def check_presence_file(path_file:str) -> bool:
    """
    Check that file is present
    """
    os.path.exists(path_file) and os.path.isfile(path_file)