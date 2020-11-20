'''
给定一个二叉查找树的节点插入顺序，请重新构建这个二叉查找树，并按从左至右顺序返回所有根节点至叶节点的路径

输入格式:
一行整数，以空格分隔
注：测试用例中不包含重复的数字

输出格式：
按照叶节点由左至右顺序，以“根节点值->节点值->...->叶节点值”输出每条路径，每行输出一条

输入样例：
5 2 6 1 3 7 4

输出样例：
5->2->1
5->2->3->4
5->6->7
'''

class BinaryTree:
    def __init__(self, num):
        self.val = num
        self.left = None
        self.right = None
        if type(num) == list:
            self.num = num[0]
            for n in num[1:]:
                self.insert(n)
        else:
            self.num = num
 
    def insert(self, num):
        bt = self
        while True:
            if num <= bt.num:
                if bt.left == None:
                    bt.left = BinaryTree(num)
                    break
                else:
                    bt = bt.left
            else:
                if bt.right == None:
                    bt.right = BinaryTree(num)
                    break
                else:
                    bt = bt.right

class Solution:
    def binaryTreePaths(self, root):
        def construct_paths(root, path):
            if root:
                path += str(root.num)
                if not root.left and not root.right:  
                    paths.append(path)  
                else:
                    path += '->' 
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)
 
        paths = []
        construct_paths(root, '')
        return paths

num = list(map(int,input().split()))
bt = BinaryTree(num)
s = Solution()
l = s.binaryTreePaths(bt)
for i in l:
    print(i)



# ints = input().split()
# tree = BinarySearchTree()
# for int in ints:
#     tree.put(int)
# res = []
# tree.get_paths(tree.root,[],res)
# for i in res:
#     print(i)

    



