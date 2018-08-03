# -------------------------------------<test1>-----------------------------
# def fishstore(fish,price): 
#     print("Fish Type: "+fish.title()+" costs $"+price)  
# 
# fish_entry=input("enter fish name:")
# price_entry=input("enter the fish price:")
# fishstore(fish_entry, price_entry)
# -------------------------------------<test2>-----------------------------
# order_amount=input("Enter cheese order weight (numeric value):")
# OA=float(order_amount)
# if OA>100:
#     print(OA,"is more than currently available stock")
# elif OA<1:
#     print(OA,"is below minimum order amount")
# else:
#     print(OA,"costs $",OA*7.99)
# -------------------------------------<test3>-----------------------------
# def Input2():
#     while True: 
#         B=input('enter word or integer:')   
#         if B:break
#     return B
# 
# A=Input2()       
# if A.isdigit():
#     if int(A)>99:
#         print(A,"is a pretty big number")
#     else:
#         print(A,"is a smaller number than expected") 
# elif A.isalpha():
#     print(A,"is all alphabetical characters!")
# else:
#     print(A,"multiple character types")
# -------------------------------------<test4>-----------------------------
def report_type():
    while True: 
        B = input('Chooes report type ("A" or "T"):')   
        if B == "A" or B == "a":
            A_type()           
            break
        elif B == "T" or B == "t":
            T_type()           
            break
        else: print(B, 
                    'is invalid type')

     
def A_type():
    item = []
    tol = 0
    while True:         
        A1 = input('Enter an integer or "Q":')
        if A1 == "Q" or A1 == "q":
            print("\nitems\n", item)
            break
        elif A1.isdigit():
#             print(A1,"\n")
            tol = tol + int(A1)
            item.append(A1)
        else: print(A1, 'is invalid type')
    print('Tol:\n', tol)

 
def T_type():
    tol = 0
    while True:         
        A2 = input('Enter an integer or "Q":')
        if A2 == "Q" or A2 == "q":
            break
        elif A2.isdigit():
            tol = tol + int(A2)
        else: print(A2, 'is invalid type')
    print('\nTol:', tol)            


report_type()            
            
            
