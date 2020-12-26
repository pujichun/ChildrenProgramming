string = "a1 b2 c d4 !!! 5"
string = input()
lst = list(string)
letter = 0
space = 0
number = 0
other = 0
for c in string:
    # 判断字符是不是英文字母
    if c.isalpha():
        letter += 1
    # 判断字符是不是数字字符
    elif c.isdigit():
        number += 1
    # 判断字符是不是空格
    elif c == " ":
        space += 1
    # 字符是其他字符
    else:
        other += 1
print(f"英文字母：{letter}")
print(f"空格：{space}")
print(f"数字：{number}")
print(f"其他字符：{other}")