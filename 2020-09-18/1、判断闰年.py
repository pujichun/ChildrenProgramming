
"""
输入年份，判断是否闰年
能够被4整除但是不能被100整数，或者能够被400整除的年份是闰年

"""

year = int(input("输入年份："))

is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

if is_leap:
    print(f"{year}是闰年")
else:
    print(f"{year}是平年")