import os

for i in os.walk(os.getcwd()):
    if os.path.isdir(i[0]):
        print(i[0])
