
# 有5个人，问5个人的年龄是多少，他说他比第4个人大2岁，问第4个人多少岁，
# 他说他比第3个人大2岁…………问第2个人多少岁，他说他比第1个人大两岁，问第1个多少岁，第一个人说他10岁

def recursionage(n):
    if n == 1:
        return 10
    return 2 + recursionage(n-1)

if __name__ == "__main__":
    age = recursionage(5)
    print(age)
