import random
target = random.randint(1,100)
# print(target)
guess = 1
# ctrl + / 註解快捷鍵
while True:
    guess = int(input('請輸入1-100的數字，輸入0離開遊戲 >> '))
    if target == guess or guess == 0:
        break    #離開迴圈
    if guess > target:
        print('數字太大')
    else:
        print('數字太小')
if guess == 0:
    print("下次再玩")
else:
    print("猜中數字 = " + str(target))




