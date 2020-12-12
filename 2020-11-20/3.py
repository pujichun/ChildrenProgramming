def isPalindrome(num):
    sum = 0
    a = num
    for i in range(len(str(a))):
        c = a % 10
        a = a // 10
        sum = sum * 10 + c
    if sum == num:
        return True
    else:
        return False

print(isPalindrome(123321))
print(isPalindrome(12343213))
