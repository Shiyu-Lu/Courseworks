def findMax(trees, honey):
    max_num = 0
    rest = honey    # 初始化rest为honey原始值
    for i in range(len(trees)):
        peach_cnt = 0   # 用来数以第i棵树为起点，最大能摘多少颗桃子
        for j in range(i, len(trees)):
            rest -= trees[j][1]     # 每次先减掉当前树的马蜂数
            if rest >= 0:       # 如果蜂蜜足够的话
                peach_cnt += trees[j][0]    # 加上这棵树的桃子
            else:
                break   # 如果蜂蜜不足，以第i棵树为起点的情况就停止了，跳出这个循环。当然不加这个break也行，只是相当于提前终止了。不加的话还在循环里，但是因为rest<0，所以peach_cnt也不会变。
        if peach_cnt > max_num: # 如果以第i棵树为起点最大的桃子数大于当前的最大值
            max_num = peach_cnt # 更新最大值
        rest = honey # 把rest重新置为honey，开始计算以第i+1棵树为起点的情况
    return max_num

while True:
    trees = []
    honey = int(input().strip())
    if honey == -1:
        break
    nums = input().strip().split()
    while True:
        peach_num = int(nums[0])
        bee_num = int(nums[1])
        if peach_num == -1 and bee_num == -1:
            print(findMax(trees, honey))
            break
        else:
            trees.append((peach_num, bee_num))
        nums = input().strip().split()