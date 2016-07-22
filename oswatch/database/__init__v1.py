import sys
import os
import configparser

# Project Information
PROJECT_INFO={
    'project_name':'__oswatch__',
    'project_author':'Abelit',
    'project_email':'ychenid@live.com',
    'project_version':'v3.14',
    'project_date':'2016-07-01'
    }

# class PathGet(object):
#     """docstring for PathGet"""
#     def __init__(self, file=PROJECT_INFO['project_name']):
#         super(PathGet, self).__init__()
#         self.file = file
        
#     def get_separator(self):
#         if 'Windows' in platform.system():
#             separator = '\\'
#         else:
#             separator = '/'
#         return separator

#     def get_path(self):
#         os_path = os.getcwd()
#         separator = self.get_separator()
#         str = os_path
#         str = str.split(separator)
#         while len(str) > 0:
#             spath = separator.join(str)+separator+self.file
#             leng = len(str)
#             if os.path.exists(spath):
#                 return spath
#             str.remove(str[leng-1])
            
#     def get_dir(self):
#         return os.path.dirname(self.get_path())

class DirGet:
    """docstring for DirGet"""
    def __init__(self, arg):
        super(DirGet, self).__init__()
        self.arg = arg

    def get_dir(self): 
        realpath=os.path.realpath(self.arg)
        if os.path.isdir(self.arg):
            path=self.arg
        else:
            path=os.getcwd()
            realpath=os.getcwd()
        dirlist=[]
        if realpath=='/':
            for i in os.listdir(path):
                if os.path.isdir(realpath+i):
                    dirlist.append(realpath+i)
            dirlist.append(realpath)
        else:
            for i in os.listdir(path):
                if os.path.isdir(realpath+'/'+i):
                    dirlist.append(realpath+'/'+i)
            dirlist.append(realpath)
        return dirlist


# Add env path
dirs=DirGet('../').get_dir()
for i in dirs:
	sys.path.append(i)

# 
if __name__=='__main__':
    print("The dirs under current dir:")
    print(DirGet('../').get_dir())
    print("The env:")
    print(sys.path)
   
