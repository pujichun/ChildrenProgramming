a = "I love you, my baby."
b = "You are a good boy."
c = "We are very happy with you."

# 1. 将字符串拼接在一起
# 2. 找出里面的有哪些英文字符
#     - 去重（去掉重复的字符）
# 3. 计算英文字符出现的次数

abc = a + b + c
print(abc)
abc = abc.upper()
letterList = sorted(list(set(abc)))
print(letterList)
# [(A, 2), (B, 10)]
tupList = []
for c in letterList:
    if c.isalpha():
        temp = c, abc.count(c)
        tupList.append(temp)
# tupList = sorted(tupList)
for tup in tupList:
    print(f"{tup[0]}", end="\t")
print()
for tup in tupList:
    print(f"{tup[1]}", end="\t")


