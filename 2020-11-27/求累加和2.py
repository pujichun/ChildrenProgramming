def foo():
    n = int(input("请输入要相加的数字："))
    m = int(input("请输入要相加的次数："))
    lis = []
    a = 0
    for i in range(m):
        a += n * (10 ** i)
        lis.append(a)
    print(f"结果{sum(lis)}")

if __name__ == "__main__":
    foo()