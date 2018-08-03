'''
Created on 2018年7月19日

@author: Student
'''
class MyBase:
    
    coeff=2
    
    def __init__(self,x):
        self.x=x
    
    def mult(self):
        return self.coeff*self.x
    
    
class MyDeriv(MyBase):
    
    coeff=3
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
#     def __init__(self,x,y,z):
#        self.x=x
#        self.y=y
#        self.z=z
#        print(self.x,self.y,self.z)
#         
    def mult2(self):
        return self.coeff*self.x*self.y
    
a=MyBase(3)
print(a.mult())

b=MyDeriv(-1,2)
# c=MyDeriv(-1)
# print(c.x)
print(b.mult())
print(b.mult2())
print(b.coeff)


def mult3(y):
        return y
