class MyClass1():
    x=0
    y=0
    def my_print(self):
        self.x += 1
        MyClass1.y += 2
        print('(x,y)=({},{})'.format(self.x,self.y))
        
f=MyClass1
a=MyClass1()
b=f()
a.my_print()
b.my_print()
b.my_print()
print('\n')        
# -------------------------------------------------------------------        
        
class MyClass2():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def my_print(self):
        self.x += 1
        self.y += 2
#         MyClass2.y += 2
        print('(x,y)=({},{})'.format(self.x,self.y))

a=MyClass2(2,3)
b=MyClass2(-1,5)

a.my_print()
b.my_print()
b.my_print()        

# def main():
#     print ('123')
#  
#  
# if __name__ =='__main__':
#     main()    
    
        
        
        