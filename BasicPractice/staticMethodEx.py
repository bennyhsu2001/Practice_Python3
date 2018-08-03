'''
Created on 2018年7月20日

@author: Student
'''

class ABC():
#     a=0
    def __init__(self, a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    @staticmethod       #步操作實例即可呼叫靜態方法
    def aaa():
        ABC.a = 10
        return ABC.a
    
    @staticmethod
    def bbb(self, b):
        self.b=b
        return self.b
    
    @staticmethod
    def ccc(c):
        return c
    
    def abc(self):
        return self.a
    
x=ABC(1,2,3)
print(x.aaa())

# print(ABC.bbb(4))

print(ABC.ccc(5))

print(x.abc())


