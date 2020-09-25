# 三角形的面积等于三边和的一半与分别减去三边后的乘积的二分之一次方

def area(x, y, z):
    c = (x + y + z)/2
    s = (c*(c-x)*(c-y)*(c-z)) ** 0.5
    return s


# 而eval()会去掉字符串最外层的引号
x = eval(input("请输入三角形的第一条边: "))
y = eval(input("请输入三角形的第二条边: "))
z = eval(input("请输入三角形的第三条边: "))
s = area(x, y, z)
print(f"s={s}")

# 函数参数的传递
# 如果传递时不指定形式参数对应的实际参数，那么就会按照顺序传递


def bar(j, k, l):
    print(j)
    print(k)
    print(l)


j = 1
k = 2
l = 3
bar(k, j, l)
