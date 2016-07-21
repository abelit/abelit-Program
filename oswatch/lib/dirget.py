import os

class DirGet:
    """docstring for DirGet"""
    def __init__(self, arg):
        super(DirGet, self).__init__()
        self.arg = arg

    def show_dir(self): 
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

if __name__=='__main__':
    print(DirGet('../').show_dir())
