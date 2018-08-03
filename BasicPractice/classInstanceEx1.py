'''
Created on 2018年7月30日

@author: Student
'''
class MyClass1():
    x=0;
    y=0;
    def my_print1(self):
        x=3;    #為區域變數
        y=4;
        
        self.x+=1;  
        self.y+=2;
        self.z=6;
        z=5;        #WTH
        print('(self.x,self.x2)=',self.x,self.y);
        print('(my_print.x,my_print.x2)=',x,y);
    
    def you_print(self):
        MyClass1.my_print1(self);
        
        
a=MyClass1();
print('before my_print: (a.x,a.y)=',a.x,a.y);
a.my_print1();
print('after my_print: (a.x,a.y,a.z)=',a.x,a.y,a.z);

a.you_print();

b=MyClass1();
print('(b.x,b.y)=',b.x,b.y);

#------------------------------------------------------------------

