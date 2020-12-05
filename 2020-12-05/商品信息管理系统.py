lst = []

while True:
    s = input("""请选择功能
1. 显示所有商品
2. 查询商品价格
3. 添加商品信息
4. 删除商品
输入Q或q退出\n""")
    if s == "1":
        if len(lst) == 0:
            print("没有商品，请重新选择功能")
            continue
        for i in lst:
            print(f"商品编号{i[0]}, 商品名称：{i[1]}, 商品价格：{i[2]}")
    elif s == "2":
        if len(lst) == 0:
            print("没有商品，请重新选择功能")
            continue
        num = input("请输入要查询的商品编号：")
        for i in lst:
            if i[0] == num:
                print(i[2])
                continue
    elif s == "3":
        msg = tuple(eval(input("请输入商品信息（编号,品名,价格）")))
        lst.append(msg)
    elif s == "4":
        if len(lst) == 0:
            print("没有商品，请重新选择功能")
            continue
        num = input("请输入要删除的商品编号：")
        for i in range(len(lst)):
            if lst[i][0] == num:
                del lst[i]
                print(f"成功删除编号为{num}的商品")
                break
        else:
            print(f"没有编号为{num}的商品")
    elif s == "Q" or s == "q":
        break
