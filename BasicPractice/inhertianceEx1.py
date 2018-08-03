'''
Created on 2018年7月30日

@author: Student
'''
class dad:
    x=1;
    y=1;
    def __init__(self,a):
        self.a=a+1;
    
    
class mom:
    x=2;
    y=0;
    z=3;
    
    
class son(dad, mom):
    def DNA(self):
        print(self.z);

Mike=son();
Mike.DNA();