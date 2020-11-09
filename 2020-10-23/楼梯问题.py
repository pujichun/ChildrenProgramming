# 有n级台阶，每次只能走1步或2步，问有走大顶层有多少种走法

def floor(n):
    if n < 3:
        return n
    return floor(n-1) + floor(n-2)

if __name__ == "__main__":
    print(floor(5))