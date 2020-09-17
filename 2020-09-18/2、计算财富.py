
"""
假设你有100元钱，现在你有一个投资渠道，可以每年获得10%的利息
如此，一年以后你便拥有了100×1.1=110元，两年以后你便拥有了100×1.1×1.1=121元

"""

n = int(input("输入年数:"))

money = 100
for i in range(n):
    money = money * 1.1
print(f"{n}年以后的财富值为{money:.2f}")

# 相当于是100乘以1.1的n次方
# money = 100
# money = money * pow(1.1, n)
# print(money)