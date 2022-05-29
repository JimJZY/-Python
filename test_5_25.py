import  random
secret = random.randint(1,10)
print('---------我爱鱼C工作室-----------')
temp = input("不妨猜一下小甲鱼心里想的那个数字:")
guess = int(temp)
while guess != secret:
    temp = input("猜错了，请重新输入:")
    guess = int(temp)
    if guess == secret:
        print("猜对了")
    else:
        if guess > secret:
            print("大了大了")
        else:
            print("小了小了")

print("游戏结束")
