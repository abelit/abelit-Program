__metaclass__=type

class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def setSize(self,size):
        self.width,self.height=size
    def getSize(self):
        return self.width,self.height
    size=property(getSize,setSize)


class Rectangle2:
    def __init__(self):
        self.width=0
        self.height=0
    def __setattr__(self,name,value):
        if name=='size':
            self.width,self.height=value
        else:
            self.__dict__[name]=value
    def __getattr__(self,name):
        if name=='size':
            return self.width,self.height
        else:
            raise AttributeError


class myClass:
    @staticmethod
    def smeth():
        print("This is a static method")
    #smeth=staticmethod(smeth)

    @classmethod
    def cmeth(cls):
        print('This is a class method of',cls)
    #cmeth=classmethod(cmeth)



