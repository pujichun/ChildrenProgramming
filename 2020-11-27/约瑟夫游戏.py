def main():
    n, m = map(int, input().split())
    l = [i for i in range(1, n+1)]
    squ = []
    index = 0
    while l:
        temp = l.pop(0)
        index += 1
        if index == m:
            index = 0
            squ.append(str(temp))
        else:
            l.append(temp)
    print(" ".join(squ))


def foo():
    n = int(input())
    peopels = []
    for i in range(1, n+1):
        peopels.append(i)
    index = 0
    while len(peopels) != 1:
        t = peopels.pop(0)
        index += 1
        if index == 3:
            index = 0
        else:
            peopels.append(t)
    print(peopels[0])


if __name__ == "__main__":
    foo()