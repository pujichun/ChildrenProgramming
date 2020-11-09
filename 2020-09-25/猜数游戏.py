import random


# 生成随机数，猜这个数是多少
rnd = random.randint(1, 100)


# while循环实现
temp = 7
while temp > 0:
    guess = int(input(f"请猜1~100之间的随机数，你有{temp}次机会："))
    if guess == rnd:
        print(f"恭喜你，第{8-temp}次机会猜对了！")
        break
    elif guess > rnd:
        temp -= 1
        print(f"大了！你还有{temp}次机会！")
    else:
        temp -= 1
        print(f"小了！你还有{temp}次机会！")
    if temp == 0:
        print(f"很遗憾，7次机会用尽都没猜到！正确数是{rnd}")

# for循环实现
for i in range(7, 0, -1):
    guess = int(input(f"请猜1~100之间的随机数，你还有{i}次机会："))
    if guess == rnd:
        print(f"恭喜你，第{8-i}次机会猜对了！")
        break
    elif guess > rnd:
        print(f"大了！你有{i-1}次机会！")
    else:
        print(f"小了！你有{i-1}次机会！")
else:
    print(f"很遗憾，7次机会用尽都没猜到！正确数是{rnd}")
