'''
Created on 2018年7月20日

@author: Student
'''
class CoefVar():
    coef=1
    
#     @classmethod
    def mul(cls, fact):
        return cls.coef*fact
    
class MulFive(CoefVar):
    coef=5
    
# x=MulFive.mul(4)
x=MulFive
print(x.mul(4))

# print(x)