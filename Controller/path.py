import os


class __PATH__():
    def __init__(self):
        pass

    def get_path(self):
        return os.getcwd()

    def set_path(self, path):
        os.chdir(path)
    
    def get_files(self):
        __IMAGE__ = [i for i in os.listdir()]
        return __IMAGE__
