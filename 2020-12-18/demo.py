# 任意输入一句话：
# （1）请问：不重复的字符共有多少个？它们是哪些？
# （2）请问：不重复的字符或文字共有多少个？它们是哪些？
# （3）请问：不重复的英文字符共有多少个？它们是哪些？
# （4）请问：不重复的英文字符（不区分大小写）共有多少个？它们是哪些？

def func1():
    string = "你好！Lucky！"
    s = set(string)
    print(len(s))
    print(s)

def func2():
    string = "你好！Lucky！"
    l = list(string)
    s = set(string)
    print(len(l))
    print(s)

def func3():
    string = "你好！Lucky！"
    length = []
    s = set()
    for c in string:
        if 97 <= ord(c) <= 122 or 65 <= ord(c) <= 90:
            s.add(c)
            length.append(c)
    print(s)
    print(len(length))

def func4():
    string = "你好！Lucky！"
    string = string.upper()
    length = []
    s = set()
    for c in string:
        if 65 <= ord(c) <= 90:
            s.add(c)
            length.append(c)
    print(s)
    print(len(length))

func2()
