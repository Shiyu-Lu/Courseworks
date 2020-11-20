'''
一个专业的小偷决定连夜搜刮沿街的房子。每间房都藏有一定的现金;
但需要注意的是，这条街上相邻的房间都装有连通的报警系统，一旦相邻的房间同时被偷则会自动报警。
请规划方案，使不触发报警器的前提下获得最大的收益。

输入格式:
一行非负整数序列，代表沿街每个房间的收益

输出格式：
一个整数，代表可能的最大收益

输入样例：
2 1 2 3

输出样例：
5
注：同时偷窃下标为 0（收益2）与 3（收益3）的房间，可以获得最大收益5
'''

def rob(nums):
    if not nums:
        return 0
    length = len(nums)
    if length == 1:
        return nums[0]
    if length == 2:
        return max(nums[0], nums[1])
    auxiliary = [-1] * (length + 1)
    auxiliary[0] = 0
    auxiliary[1] = nums[0]
    for index in range(1, length):
        auxiliary[index + 1] = max(auxiliary[index], auxiliary[index - 1] + nums[index])
    return auxiliary[-1]


values = input().split()
values = [int(x) for x in values]
print(rob(values))