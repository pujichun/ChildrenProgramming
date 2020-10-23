"""
递归函数：在函数中调用这个函数本身

第一个数和第二个数都是1，从第三个数开始，后面的数都等于前面的两个数的和
我们将第一项设为x，第二项也为x，那么后面的数可以表示为 第三个:x+x，第四个:x+x+x

"""



def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    result = fib(6)
    print(result)