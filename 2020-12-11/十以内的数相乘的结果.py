# 两个[1,9]的随机数相乘，请问运算结果有多少种？有哪些数

s = set()
for i in range(1, 10):
    for j in range(1, 10):
        s.add(i*j)
print(len(s))
for i in s:
    print(i, end=" ")
