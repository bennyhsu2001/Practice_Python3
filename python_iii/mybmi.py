# mybmi.py
name = None

def bmi(hei, wei):
    val = wei/hei/hei
    return val
    
if __name__ == '__main__':
    print('BMI with 160cm height and 50kg weight :',
          bmi(1.60,50))
