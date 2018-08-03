'''
Created on 2018年7月30日

@author: Student
'''
pi=3.14;

def Pi1():
    print(pi);
    
def Pie1():
    print("pie");
    print (__name__);
    
Pie1(); #檔案為一class，python class中可直接執行方法，被import後會直接執行

if __name__=='__main__':
    Pi1();      #被import後不會執行
    print(__name__);