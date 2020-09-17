"""
输入三条边，判断是否能够构成三角形。
如果不能构成，则提示并结束程序；
如果能够构成三角形，判断是否构成等腰三角形，并输出结果

两边之和大于第三边
"""
a = float(input('输入第1个数：'))
b = float(input('输入第2个数：'))
c = float(input('输入第3个数：'))

if a + b > c and a + c > b and b + c > a:
    if a == b or a == c or b == c:
        print("能构成等腰三角形")
    else:
        print("能构成三角形，但不能构成等腰三角形")
else:
    print("不能构成三角形")

# 使用set快速判断是否有元素相等