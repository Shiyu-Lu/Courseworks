def dpWordEdit(original, target, oplist):
    score = 0
    operations = []
    insert = oplist['insert']
    delete = oplist['delete']
    m, n = len(original), len(target)
    def copy(source, target):
        if target == source:
            return oplist['copy']
        else:
            return oplist['delete'] + oplist['insert']
    dpTable = [[0 for j in range(m+1)] for i in range(n+1)]
    count = 0
    for i in dpTable:
        i[0] = insert * count
        count += 1
    count = 0
    for j in range(m+1):
        dpTable[0][j] = delete * count
        count += 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            insertCost = dpTable[i-1][j] + insert
            deleteCost = dpTable[i][j-1] + delete
            copyCost = dpTable[i-1][j-1] + copy(original[j-1], target[i-1])
            dpTable[i][j] = min(insertCost, deleteCost, copyCost)
    score = dpTable[n][m]   # 获得总得分
    i, j = n, m
    while i > 0 and j > 0:
        if dpTable[i][j] == dpTable[i-1][j-1] + copy(original[j-1], target[i-1]):
            operation = 'copy' + '(%s)'%original[j-1]
            i -= 1
            j -= 1
            operations.insert(0,operation)
        elif dpTable[i][j] == dpTable[i-1][j] + insert:
            operation = 'insert' + '(%s)'%target[i-1]
            i -= 1
            operations.insert(0,operation)
        elif dpTable[i][j] == dpTable[i][j-1] + delete:
            operation = 'delete' + '(%s)'%original[j-1]
            j -= 1
            operations.insert(0,operation)       

    return score, operations


# 检验
print("========= 2 单词最小编辑距离问题 =========")
oplist = {'copy': 5, 'delete': 20, 'insert': 20}
originalWords = [
    "cane", "sheep", "algorithm", "debug", "difficult", "directory",
    "wonderful"
]
targetWords = [
    "new", "sleep", "alligator", "release", "sniffing", "framework", "terrific"
]

for i in range(len(originalWords)):
    score, operations = dpWordEdit(originalWords[i], targetWords[i], oplist)
    print(score)
    print(operations)

# 操作所对应的分数可调整
# oplist = {'copy':5, 'delete':20, 'insert':20}
# 70
# ['delete c', 'delete a', 'copy n', 'copy e', 'insert w']
# 60
# ['copy s', 'insert l', 'delete h', 'copy e', 'copy e', 'copy p']
# 185
# ['copy a', 'copy l', 'insert l', 'insert i', 'copy g', 'insert a', 'insert t', 'copy o', 'copy r', 'delete i', 'delete t', 'delete h', 'delete m']
# 205
# ['insert r', 'delete d', 'copy e', 'insert l', 'insert e', 'insert a', 'insert s', 'insert e', 'delete b', 'delete u', 'delete g']
# 200
# ['insert s', 'insert n', 'delete d', 'copy i', 'copy f', 'copy f', 'copy i', 'insert n', 'insert g', 'delete c', 'delete u', 'delete l', 'delete t']
# 220
# ['insert f', 'delete d', 'delete i', 'copy r', 'insert a', 'insert m', 'copy e', 'insert w', 'delete c', 'delete t', 'copy o', 'copy r', 'insert k', 'delete y']
# 235
# ['insert t', 'delete w', 'delete o', 'delete n', 'delete d', 'copy e', 'copy r', 'insert r', 'insert i', 'copy f', 'insert i', 'insert c', 'delete u', 'delete l']
#