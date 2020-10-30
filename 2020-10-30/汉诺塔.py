step=0

# 从 a 柱借助 b 柱移到 c 柱
# a b c并不是真正的A B C柱，而是以a这个变量中的值为起点，b中的变量为辅助，移到c中的变量的过程
# 我们只需要考虑极端情况，从哪里开始移动，以谁为辅助，移动到哪
# 最终情况前，我们肯定是只剩下了两个圆盘在B上，那么 我们需要将B上下面的那个移动到C，那么就要以B为起点，A为辅助移动到C

def HanoiTower(a, b, c, n):
    global step
    if n == 1:
        step+=1
        print(f'{step}:{a}-->{c}')
    else:
        HanoiTower(a, c, b, n - 1)
        step+=1
        print(f'{step}:{a}-->{c}')
        HanoiTower(b, a, c, n - 1)


HanoiTower('A', 'B', 'C', 2)

