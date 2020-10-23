def floor(n):
    if n < 3:
        return n
    return floor(n-1) + floor(n-2)

if __name__ == "__main__":
    print(floor(5))