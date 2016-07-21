import sys
import os
from dirget import DirGet

dirs=DirGet('./').show_dir()

for i in dirs:
	sys.path.append(i)

if __name__=='__main__':
    print(sys.path)
