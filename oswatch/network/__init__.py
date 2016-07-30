import sys
import os
import platform
import configparser

# Project Information
PROJECT_INFO={
    'project_name':'__oswatch__',
    'project_author':'Abelit',
    'project_email':'ychenid@live.com',
    'project_version':'v3.14',
    'project_date':'2016-07-01'
    }

class PathGet(object):
    """docstring for PathGet"""
    def __init__(self, file):
        super(PathGet, self).__init__()
        self.file = file
        
#    def get_separator(self):
#        if 'Windows' in platform.system():
#            separator = '\\'
#        else:
#            separator = '/'
#        return separator

    def get_path(self):
        os_path = os.getcwd()
       # separator = self.get_separator()
        separator = os.sep
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

# class DirGet:
#     """docstring for DirGet"""
#     def __init__(self, arg):
#         super(DirGet, self).__init__()
#         self.arg = arg

#     def get_dir(self): 
#         realpath=os.path.realpath(self.arg)
#         if os.path.isdir(self.arg):
#             path=self.arg
#         else:
#             path=os.getcwd()
#             realpath=os.getcwd()
#         dirlist=[]
#         if realpath=='/':
#             for i in os.listdir(path):
#                 if os.path.isdir(realpath+i):
#                     dirlist.append(realpath+i)
#             dirlist.append(realpath)
#         else:
#             for i in os.listdir(path):
#                 if os.path.isdir(realpath+'/'+i):
#                     dirlist.append(realpath+'/'+i)
#             dirlist.append(realpath)
#         return dirlist

class BaseConfig(object):
    """docstring for BaseConfig"""
    def __init__(self, basepath=PROJECT_INFO['project_name']):
        super(BaseConfig, self).__init__()
        self.basepath = basepath
    # Add env path
    def add_env(self): 
        for j in os.walk(PathGet(self.basepath).get_dir()):
            if os.path.isdir(j[0]):
                sys.path.append(j[0])
# Add env   

BaseConfig().add_env()

if __name__=='__main__':
    BaseConfig().add_env()
    print(sys.path)
