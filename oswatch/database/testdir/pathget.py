import os
import platform

class PathGet(object):
    """docstring for PathGet"""
    def __init__(self, file):
        super(PathGet, self).__init__()
        self.file = file
        
    def get_separator(self):
        if 'Windows' in platform.system():
            separator = '\\'
        else:
            separator = '/'
        return separator

    def get_path(self):
        os_path = os.getcwd()
        separator = self.get_separator()
        str = os_path
        str = str.split(separator)
        while len(str) > 0:
            spath = separator.join(str)+separator+self.file
            leng = len(str)
            if os.path.exists(spath):
                return spath
            str.remove(str[leng-1])
    def get_dir(self):
        return os.path.dirname(self.get_path())

if __name__ == '__main__':
    print(PathGet('__oswatch__.py').get_dir())