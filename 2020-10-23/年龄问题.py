


def recursionage(n):
    if n == 1:
        return 10
    return 2 + recursionage(n-1)

if __name__ == "__main__":
    age = recursionage(5)
    print(age)
