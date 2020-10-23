


def fn(n):
    if n == 1:
        return n
    return fn(n - 1) * n

if __name__ == "__main__":
    result = fn(4)
    print(result)