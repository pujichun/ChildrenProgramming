def fn(n):
    if n == 1:
        return 1
    return fn(n - 1) * n


n = 4
for i in range(1, n +1):
    print(fn(i))