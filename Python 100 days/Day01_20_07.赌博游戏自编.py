import random
m = 1000
while m > 0:
    print(f'玩家的总资产为{m},下注金额请不要超过{m}!')
    # 下注金额必须大于0且小于等于玩家的总资产
    debt = int(input('请下注：'))
    # 用两个1到6均匀分布的随机数相加模拟摇两颗色子得到的点数
    first_point = random.randrange(1, 7) + random.randrange(1, 7)
    print(f'\n玩家摇出的点数为{first_point}')
    if first_point in (7, 11):
        print(f'玩家赢，玩家将获得{debt}元\n')
        m += debt
    elif first_point in (2, 3, 12):
        print(f'庄家赢，玩家将失去{debt}元\n')
        m -= debt
    else:
        while True:
            # 如果第一次摇色子没有分出胜负，玩家需要重新摇色子
            current_point = random.randrange(1, 7) + random.randrange(1, 7)
            print(f'玩家摇出的点数为{current_point}')
            if current_point == first_point:
                print(f'玩家赢，玩家将获得{debt}元\n')
                m += debt
                break
            elif current_point == 7:
                print(f'庄家赢，玩家将失去{debt}元\n')
                m -= debt
                break
print('游戏终止，玩家总资产已耗尽')



