def foo():
    n = int(input("请输入要相加的数字："))
    m = int(input("请输入要相加的次数："))
    num, a = 0, 0
    for i in range(m):
        a += n * (10 ** i)
        num += a 
    print(num)

if __name__ == "__main__":
    foo()