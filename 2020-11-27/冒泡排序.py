def foo():
    arr = input()
    arr = arr.split(",")
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        for j in range(0, n-i-1):
            if int(arr[j]) > int(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(",".join(arr))


if __name__ == "__main__":
    foo()
