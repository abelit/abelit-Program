class Bird(object):
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry=False
        else:
            print('No, thanks!')
class SongBird(Bird):
    def __init__(self):
        super(SongBird,self).__init__()
        self.sound='Squawk!'
    def sing(self):
        print(self.sound)

    
#!/usr/bin/env python 
#coding:utf-8

##
##class Father(object):#新式类
##    def __init__(self):
##        self.name='Liu'
##        self.FamilyName='Yan'
##        
##    def Lee(self):
##        print('我是父类函数Lee')
##    
##    def Allen(self):
##        print("我是父类函数Allen")
##        
##class Son(Father):
##    def __init__(self):
##        #Father.__init__(self)  #经典类执行父类构造函数
##        super(Son,self).__init__()  #新式类执行父类构造函数
##        self.name='Feng'
##        
##    def Aswill(self): #子类新增函数
##        print('Son.Bar')
##    
##    def Lee(self):#重写父类函数Lee
##        print('子类重写了父类函数Lee')
