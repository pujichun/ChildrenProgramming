lst = [("001", "可乐", 3.99), ("002", "面包", 2), ("003", "电脑", 3000)]
bought = []

m = eval(input("请输入你的工资："))

while True:
    for i in lst:
        print(f"商品编号：{i[0]}, 商品名称：{i[1]}, 商品价格：{i[2]}")
    t = input("请输入你要购买的商品编号：")
    for i in lst:
        if t == i[0]:
            if m < i[2]:
                print("你的余额不足")
            else:
                m = m - i[2]
                print("购买成功")
                bought.append(i)
            break
    con = input("是否继续购买？(输入是或否)")
    if con == "否":
        print(f"你的余额为{m}, 购买的商品如下：")
        for i in bought:
            print(f"商品编号：{i[0]}, 商品名称：{i[1]}, 商品价格：{i[2]}")
        break
