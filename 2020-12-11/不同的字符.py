# 从键盘上随机输入一个字符串，请问不同的字符有多少个？具体是哪些字符？

string  = input("请输入一个字符串：")
s = set(string)
print(len(s))
for i in s:
    print(i, end=" ")
