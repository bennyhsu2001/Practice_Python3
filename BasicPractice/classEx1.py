'''
Created on 2018年7月20日

@author: Student
'''
class add():
    x=1
    y=2
    
    def add1(x,y):
        add.x=x
        add.y=y
#         self.x=x    //Error
        
    
    def add2(self,x,y):
        print((self.x+x),'\n',(self.y+y))
        

# a=add()
add.add1(3,4)
b=add()
b.add2(5,6)