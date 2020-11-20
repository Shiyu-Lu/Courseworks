#uuid_share#  2ab430a7-276d-4893-85d0-38d92bc77a65  #
# SESSDSA20课程上机作业
# 【H5】AVL树作业
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中指定部位编写代码
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
# （4）作业代码部分在4月29日18:00之前提交到PyLn编程学习系统，班级码见Canvas系统

# ---- 用AVL树实现字典类型 ----
# 用AVL树来实现字典类型，使得其put/get/in/del操作均达到对数性能
# 采用如下的类定义，至少实现下列的方法
# key至少支持整数、浮点数、字符串
# 请调用hash(key)来作为AVL树的节点key
# 【注意】涉及到输出的__str__, keys, values这些方法的输出次序是AVL树中序遍历次序
#    也就是按照hash(key)来排序的，这个跟Python 3.7中的dict输出次序不一样。

# 请在此编写你的代码
import struct
from hashlib import md5

def hash(k):
    if isinstance(k,str):
        return md5(k.encode()).hexdigest()
    elif isinstance(k,int):
        return md5(struct.pack('d',k)).hexdigest()
    elif isinstance(k,float):
        return md5(struct.pack('f',k)).hexdigest()

class TreeNode:   # 创建树的节点类
    """
    二叉树节点
    请自行完成节点内部的实现，并实现给出的接口
    """
    def __init__(self,key,val=None,left=None,right=None,parent=None):  # 初始化方法
        self.key = hash(key)                     # 节点hash值，节点位置
        self.ori_key = key                       # 原key，索引
        self.payload = val                       # 有效载荷，节点显示的值
        self.left = left                         # 左字节点
        self.right = right                       # 右字节点
        self.parent = parent                     # 父节点
        self.balanceFactor = 0                   # 平衡因子

    def __iter__(self):   # 中序遍历的生成器/迭代器
        if self.getLeft():                # 若左子节点存在
            for ori_key in self.left:     # 循环输出当前节点的左子树的节点值
                yield ori_key             # 在for循环中，每次执行到yield时，就返回一个迭代值，且不会终止循环；下个循环时，代码从yield返回值的下一行继续返回
        yield self.ori_key                # 返回当前节点值
        if self.getRight():               # 若右子节点存在
            for ori_key in self.right:    # 循环输出当前节点的右子树的节点值
                yield ori_key

    def getLeft(self):  # 获取左子树（不存在时返回None）
        return self.left

    def getRight(self):  # 获取右子树（不存在时返回None)
        return self.right

    def isLeft(self):   # 判断是否是左子节点（父节点存在，并且self与self父节点的左子节点相同）
        return self.parent and self.parent.left == self
    
    def isRight(self):   # 判断是否是右子节点
        return self.parent and self.parent.right == self
    
    def isRoot(self):   # 判断是否是根结点（没有父节点）
        return not self.parent

    def isLeaf(self):   # 判断是否是叶节点（没有左右子节点）
        return not (self.right or self.left)

    def hasAnyChildren(self):   # 判断是否有子节点（有左或右节点）
        return self.right or self.left
    
    def hasBothChildren(self):   # 判断是否有2个子节点（有左右2个子节点）
        return self.right and self.left

    def replaceNodeData(self,key,value,lc,rc):   # 替换节点数据
        self.key = hash(key)                 # 更新节点hash值
        self.ori_key = key                   # 更新节点值
        self.payload = value                 # 更新有效载荷
        self.left = lc                       # 更新左子节点
        self.right = rc                      # 更新右子节点
        if self.getLeft():                   # 若有左子节点，将该节点的左子节点的父节点指向self
            self.left.parent = self
        if self.getRight():                  # 若有右子节点，将该节点的右子节点的父节点指向self
            self.right.parent = self

    def replaceNodeValue(self,key,val):   # 替换节点有效载荷
        self.key = hash(key)        # 更新节点值
        self.ori_key = key          # 更新节点原key
        self.payload = val          # 更新有效载荷

    def findSuccesor(self):   # 查找被删除节点的继任者，继任者节点最多只能有一个子节点
        succ = None                                      # 初始化被删除节点的继任者为None
        if self.getRight():                              # 若被删除节点有右子节点，
            succ = self.right.findMin()                  # 获取被删除节点的右子树中的最小节点作为继任者
        else:                                            # 若被删除节点没有右子节点
            if self.parent:                              # 若被删除节点有父节点
                if self.isLeft():                        # 若被删除节点是父节点的左子节点
                    succ = self.parent                   # 被删除节点的父节点是继任者
                else:                                    # 若被删除节点是父节点的右子节点，则被删除节点的继任者是其父节点的继任者，不会是被删除节点
                    self.parent.right = None             # 暂时将None赋值给被删除节点，则继任者不会是被删除节点，方便下一行递归查找
                    succ = self.parent.findSuccesor()    # 将被删除节点的父节点的继任者作为继任者
                    self.parent.right = self             # 获得继任者后，重新将被删除节点赋值给自己，以免被删除节点为None扰乱树结构
        return succ

    def findMin(self):   # 查找当前树的最小子节点，因AVL搜索树的左子节点的值是最小的，所以只找左子节点
        current = self                  # 将自身设置为当前节点
        while current.getLeft():        # 若当前节点有左子节点，则循环
            current = current.left      # 将当前节点的左子节点作为下一个当前节点
        return current                  # 返回最终左子节点，即此树中的最小节点
    
    def spliceOut(self):   # 将被删除节点的继任者拼接到被删除的节点位置
        if self.isLeaf():                               # 若被删除节点是叶节点，则无需再拼接
            if self.isLeft():                           # 若被删除节点是父节点的左子节点
                self.parent.left = None                 # 被删除节点为None，无需再拼接
            else:                                       # 若被删除节点是父节点的右子节点
                self.parent.right = None                # 被删除节点为None，无需再拼接
        elif self.hasAnyChildren():                     # 若被删除节点有子节点
            if self.getLeft():                          # 若被删除节点有左子节点
                if self.isLeft():                       # 若被删除节点是左子节点
                    self.parent.left = self.left        # 将被删除节点的父节点的左子节点指向被删除节点的左子节点
                else:                                   # 若被删除节点是右子节点
                    self.parent.right = self.left       # 将被删除节点的父节点的右子节点指向被删除节点的左子节点
                self.left.parent = self.parent          # 将被删除节点的左子节点的父节点指向被删除节点的父节点
            else:                                       # 若被删除节点没有左子节点，则被删除节点有右子节点
                if self.isLeft():                       # 若被删除节点是左子节点
                    self.parent.left = self.right       # 将被删除节点的父节点的左子节点指向被删除节点的右子节点
                else:                                   # 若被删除节点是右子节点
                    self.parent.right = self.right      # 将被删除节点的父节点的右子节点指向被删除节点的右子节点
                self.right.parent = self.parent         # 将被删除节点的右子节点的父节点指向被删除节点的父节点
        
class AVLtree:   # 创建平衡二叉树类
    def __init__(self):   # 初始化空二叉树
        self.root = None        # 根节点
        self.size = 0           # 二叉树的大小

    def __iter__(self):   # 迭代器
        if self.root:               # 若不是空树
            return iter(self.root)  # 返回二叉查找树根节点的迭代，即遍历二叉查找树
        return iter([])             # 如果是空树，则什么都不返回

    def __len__(self):   # 通过该方法使用len()
        return self.size

    def put(self,key,val):   #创造二叉搜索树
        if self.root:                          # 若树已经有根节点
            self._put(key,val,self.root)       # 从树的根开始，搜索二叉树
        else:                                  # 若树没有根节点
            self.root = TreeNode(key,val)      # 创建一个新的TreeNode并把它作为树的根节点
        self.size += 1                         # 增加树的大小
    __setitem__ = put                          # 可以直接调用mydict[key]进行赋值

    def _put(self,key,val,currentNode):   # 搜索树，put()的辅助函数
        ori_key = key                                                       # 将原key存入ori_key
        key = hash(ori_key)                                                 # 调用hash(key)作为AVL树的节点key
        if key < currentNode.key:                                           # 若新的键值小于当前节点键值，则搜索左子树
            if currentNode.getLeft():                                       # 若当前节点有左子树要搜索
                self._put(ori_key,val,currentNode.left)                     # 递归搜索左子树
            else:                                                           # 若当前节点无左子树要搜索
                currentNode.left = TreeNode(ori_key,val,parent=currentNode) # 创建一个新的TreeNode并把它作为当前节点的左子节点
                self.updateBalance(currentNode.left)                        # 更新当前节点的左子节点的平衡因子
        elif key == currentNode.key:                                        # 若新的键值等于当前节点键值
            currentNode.replaceNodeValue(ori_key,val)                       # 更新当前节点的有效载荷
            self.size -= 1                                                  # 由于只修改，未增加，又因put()中+1，所以此处-1
        else:                                                               # 若当前节点有右子树要搜索
            if currentNode.getRight():                                      # 递归搜索右子树
                self._put(ori_key,val,currentNode.right)                    # 若当前节点无右子树要搜索
            else:                                                           # 若新的键值>=当前节点键值，则搜索右子树
                currentNode.right = TreeNode(ori_key,val,parent=currentNode)# 创建一个新的TreeNode并把它作为当前节点的右子节点
                self.updateBalance(currentNode.right)                       # 更新当前节点的右子节点的平衡因子

    def updateBalance(self,node):   # 更新平衡因子
        if node.balanceFactor > 1 or node.balanceFactor < -1:   # 若节点的平衡因子不是-1、0、1
            self.rebalance(node)                                # 该节点再平衡
            return                                              
        if node.parent != None:                                 # 若该节点有父节点，即该节点不是根节点
            if node.isLeft():                                   # 若该节点是左子节点
                node.parent.balanceFactor += 1                  # 该节点的父节点的平衡因子+1
            elif node.isRight():                                # 若该节点是右子节点
                node.parent.balanceFactor -= 1                  # 该节点的父节点的平衡因子-1
            
            if node.parent.balanceFactor != 0:                  # 若该节点的父节点的平衡因子不为0
                self.updateBalance(node.parent)                 # 更新该节点的父节点的平衡因子

    def get(self,key):   # 根据索引key获取其对应的节点值
        if self.root:                           # 若树已经有根节点
            res = self._get(key,self.root)      # 从树的根开始，搜索二叉树
            if res:                             # 若搜索到了
                return res.payload              # 返回存储在节点的有效载荷中的值，即节点显示的值
            else:                               # 若没搜索到，则没有该索引对应的节点
                return None
        else:                                   # 若树没有根节点，则说明是空二叉树
            return None
    __getitem__ = get                           # 直接调用mydict[key]获取value
        
    def _get(self,key,currentNode):   # 搜索树，get()的辅助函数
        ori_key = key                                   # 将原key存入ori_key
        key = hash(ori_key)                             # 用hash后的key进行对比
        if not currentNode:                             # 若没有当前节点
            raise KeyError(ori_key)                     # 报错
        elif currentNode.key == key:                    # 若当前节点的位置和待查找的位置相同
            return currentNode                          # 返回当前节点的值
        elif key < currentNode.key:                     # 若当前节点的位置>待查找的位置
            return self._get(ori_key,currentNode.left)  # 递归查找当前节点的左子树
        else:                                           # 若当前节点的位置<=待查找的位置
            return self._get(ori_key,currentNode.right) # 递归查找当前节点的右子树

    def rotateLeft(self,rotRoot):   # 左旋转（右重的树要左旋转才平衡）
        newRoot = rotRoot.right                     # 待旋转节点的右子节点设为新的根节点
        rotRoot.right = newRoot.left                # 新根的原左子节点作为原根的新右子节点
        if newRoot.left != None:                    # 若新根原来有左子节点
            newRoot.left.parent = rotRoot           # 将新根的原左子节点的父节点指向原根
        newRoot.parent = rotRoot.parent             # 新根的父节点指向原根的父节点
        if rotRoot.isRoot():                        # 若原根是树的根节点
            self.root = newRoot                     # 将新根设为树的根节点
        else:                                       # 若原根不是树的根节点
            if rotRoot.isLeft():                    # 若原根是左子树
                rotRoot.parent.left = newRoot       # 将原根的父节点的左子节点指向新根
            else:                                   # 若原根是右子树
                rotRoot.parent.right = newRoot      # 将原根的父节点的右子节点指向新根
        newRoot.left = rotRoot                      # 将新根的左子节点指向原根
        rotRoot.parent = newRoot                    # 将原根的父节点指向新根
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor,0)    # 更新原根节点的平衡因子，被移动的子树内的节点的平衡因子不受旋转影响
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor,0)    # 更新新根节点的平衡因子，被移动的子树内的节点的平衡因子不受旋转影响

    def rotateRight(self,rotRoot):   # 右旋转（左重的树要右旋转才平衡）
        newRoot = rotRoot.left                      # 待旋转节点的左子节点设为新的根节点
        rotRoot.left = newRoot.right                # 新根的原右子节点作为原根的新左子节点
        if newRoot.right != None:                   # 若新根原来有右子节点
            newRoot.right.parent = rotRoot          # 将新根的原右子节点的父节点指向原根
        newRoot.parent = rotRoot.parent             # 新根的父节点指向原根的父节点
        if rotRoot.isRoot():                        # 若原根是树的根节点
            self.root = newRoot                     # 将新根设为树的根节点
        else:                                       # 若原根不是树的根节点
            if rotRoot.isRight():                   # 若原根是左子树
                rotRoot.parent.right = newRoot      # 将原根的父节点的左子节点指向新根
            else:                                   # 若原根是右子树
                rotRoot.parent.left = newRoot       # 将原根的父节点的右子节点指向新根
        newRoot.right = rotRoot                     # 将新根的右子节点指向原根
        rotRoot.parent = newRoot                    # 将原根的父节点指向新根
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor,0)    # 更新原根节点的平衡因子，被移动的子树内的节点的平衡因子不受旋转影响
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(rotRoot.balanceFactor,0)    # 更新新根节点的平衡因子，被移动的子树内的节点的平衡因子不受旋转影响
        
    def rebalance(self,node):   # 再平衡
        if node.balanceFactor < 0:                  # 若该节点的平衡因子<0
            if node.right.balanceFactor > 0:        # 若该节点的右子节点的平衡因子>0
                self.rotateRight(node.right)        # 右旋转该节点的右子节点
            self.rotateLeft(node)                   # 左旋转该节点
        elif node.balanceFactor > 0:                # 若该节点的平衡因子>0
            if node.left.balanceFactor < 0:         # 若该节点的左子节点的平衡因子<0
                self.rotateLeft(node.left)          # 左旋转该节点的左子节点
            self.rotateRight(node)                  # 右旋转该节点

    def delete(self,key):   # 根据索引key删除其对应的节点
        ori_key = key
        key = hash(ori_key)
        if self.size > 1:                                   # 若树的大小>1
            nodeToRemove = self._get(ori_key,self.root)     # 获取要删除的节点
            if nodeToRemove:                                # 若该节点存在
                self.remove(nodeToRemove)                   # 删除该节点
                self.size -= 1                              # 树的大小减1
            else:                                           # 若该节点不存在
                raise KeyError('Error,key not in mydict.')  # 报错
        elif self.size == 1 and self.root.key == key:       # 若树的大小为1，且要删除的是根
            self.root = None                                # 根节点为None
            self.size -= 1                                  # 树的大小减1
        else:                                               # 若树的大小为0，则为空树
            raise KeyError('Error, key not in mydict.')     # 报错
    __delitem__ = delete                                    # 可以直接调用del进行删除

    def remove(self,currentNode):   # 删除节点
        if currentNode.isLeaf():                                        # 若被删除节点是叶节点，则没有子节点
            if currentNode.isLeft():                                    # 若被删除节点是其父节点的左子节点
                currentNode.parent.left = None                          # 被删除节点为None
                currentNode.parent.balanceFactor -= 1                   # 父节点少了左子节点
            else:                                                       # 若被删除节点是其父节点的右子节点
                currentNode.parent.right = None                         # 被删除节点为None
                currentNode.parent.balanceFactor += 1                   # 父节点少了右子节点
            self.updateBalanceRemove(currentNode.parent)                # 从删除节点的父节点开始重新平衡
        elif currentNode.hasBothChildren():                             # 若被删除节点有2个子节点
            succ = currentNode.findSuccesor()                           # 获取被删除节点的继任者(防止树结构混乱)
            if succ.isLeft():                                           # 若继任者是左子节点，平衡因子-1，否则平衡因子+1
                succ.parent.balanceFactor -= 1
            else:
                succ.parent.balanceFactor += 1
            succ.spliceOut()                                            # 将被删除节点的继任者拼接到被删除节点位置
            currentNode.replaceNodeValue(succ.ori_key,succ.payload)     # 将被删除节点位置的值和有效载荷设置为继任者的值和有效载荷
            self.updateBalanceRemove(succ.parent)                       # 从摘除节点的父节点开始重新平衡
        else:                                                           # 若被删除节点只有1个子节点
            if currentNode.getLeft():                                   # 若被删除节点只有左子节点
                if currentNode.isLeft():                                # 若被删除节点是左子节点
                    currentNode.left.parent = currentNode.parent        # 将被删除节点的左子节点的父节点指向被删除节点的父节点
                    currentNode.parent.left = currentNode.left          # 将被删除节点的父节点的左子节点指向被删除节点的左子节点
                    currentNode.parent.balanceFactor -= 1               # 父节点少了左子节点
                elif currentNode.isRight():                             # 若被删除节点是右子节点
                    currentNode.left.parent = currentNode.parent        # 将被删除节点的左子节点的父节点指向被删除节点的父节点
                    currentNode.parent.right = currentNode.left         # 将被删除节点的父节点的右子节点指向被删除节点的左子节点
                    currentNode.parent.balanceFactor += 1               # 父节点少了右子节点
                else:                                                   # 若被删除节点无父节点，则被删除节点为根节点
                    currentNode.left.parent = None                      # 将被删除节点的左子节点设置为None
                    self.root = currentNode.left                        # 将根结点设置为被删除节点的左子节点
            else:                                                       # 若被删除节点只有右子节点
                if currentNode.isLeft():                                # 若被删除节点是左子节点
                    currentNode.right.parent = currentNode.parent       # 将被删除节点的右子节点的父节点指向被删除节点的父节点
                    currentNode.parent.left = currentNode.right         # 将被删除节点的父节点的左子节点指向被删除节点的右子节点
                    currentNode.parent.balanceFactor -= 1               # 父节点少了左子节点
                elif currentNode.isRight():                             # 若被删除节点是右子节点
                    currentNode.right.parent = currentNode.parent       # 将被删除节点的右子节点的父节点指向被删除节点的父节点
                    currentNode.parent.right = currentNode.right        # 将被删除节点的父节点的右子节点指向被删除节点的右子节点
                    currentNode.parent.balanceFactor += 1               # 父节点少了右子节点
                else:                                                   # 若被删除节点无父节点，则被删除节点为根节点
                    currentNode.right.parent = None                     # 将被删除节点的右子节点设置为None
                    self.root = currentNode.right                       # 将根结点设置为被删除节点的右子节点

            if currentNode.parent:                                  # 如果不是根结点就要重新平衡
                self.updateBalanceRemove(currentNode.parent)        # 从删除节点的父节点开始重新平衡

    def updateBalanceRemove(self,node):   # 在remove操作中重新平衡
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)                        # 重新平衡
            node = node.parent                          # 继续看newRoot的平衡因子，如果变为0，还要继续传播
        if node.balanceFactor == 0 and node.parent:
            if node.isLeft():                           # 左子节点少了
                node.parent.balanceFactor -= 1
            elif node.isRight():                        # 右子节点少了
                node.parent.balanceFactor += 1
            self.updateBalanceRemove(node.parent)       # 向上传播

class mydict:
    """
    以AVL树作为内部实现的字典
    """
    def getRoot(self):  # 返回内部的AVL树根
        return self.dict.root

    def __init__(self):  # 创建一个空字典
        self.dict = AVLtree()

    def __setitem__(self, key, value):  # 将key:value保存到字典
        # md[key]=value
        self.dict[key] = value

    def __getitem__(self, key):  # 从字典中根据key获取value
        # v = md[key]
        # key在字典中不存在的话，请raise KeyError
        if key in self.dict:
            return self.dict[key]
        else:
            raise KeyError('Error, key not in mydict.')

    def __delitem__(self, key):  # 删除字典中的key
        # del md[key]
        # key在字典中不存在的话，请raise KeyError
        del self.dict[key]

    def __len__(self):  # 获取字典的长度
        # l = len(md)
        return self.dict.size

    def __contains__(self, key):  # 判断字典中是否存在key
        # k in md 
        try:
            v = self[key]
        except KeyError:
            return False
        return True

    def clear(self):  # 清除字典
        self.__init__()

    def stringTrans(self,v):
        if isinstance(v,str):
            return '\''+v+'\''
        else:
            return str(v)

    def __str__(self):  # 输出字符串形式，参照内置dict类型，输出按照AVL树中序遍历次序
        # 格式类似：{'name': 'sessdsa', 'hello': 'world'}
        if self.dict.root:
            output = '{'
            for i in self.dict: 
                output += self.stringTrans(i)
                output += ': '
                output += self.stringTrans(self.dict[i])
                output += ', '
            output = output[:-2]
            output += '}'
            return output
        else:
            return '{}'
    __repr__ = __str__

    def keys(self):  # 返回所有的key，类型是列表，按照AVL树中序遍历次序
        keys = []
        for i in self.dict:
            keys.append(i)
        return keys

    def values(self):  # 返回所有的value，类型是列表，按照AVL树中序遍历次序
        values = []
        for i in self.dict:
            values.append(self.dict[i])
        return values


# 代码结束

#mydict=dict
# 检验
print("========= AVL树实现字典 =========")
md = mydict()
# md['hello'] = 'world'
# md['name'] = 'sessdsa'
# print(md)  # {'name': 'sessdsa', 'hello': 'world'}

# for f in range(1000):
#     md[f**0.5] = f

# for i in range(1000, 2000):
#     md[i] = i**2

# print(len(md))  # 2002
# print(md[2.0])  # 4
# print(md[1000])  # 1000000
# print(md['hello'])  # world
# print(20.0 in md)  # True
# print(99 in md)  # False

# del md['hello']
# print('hello' in md)  # False
# for i in range(1000, 2000):
#     del md[i]
# print(len(md))  # 1001
# for f in range(1000):
#     del md[f**0.5]
# print(len(md))  # 1
# print(md.keys())  # ['name']
# print(md.values())  # ['sessdsa']
# for a in md.keys():
#     print(md[a])  # sessdsa
# md.clear()
# print(md)  # {}



md.__setitem__(6,6)
md.__len__()
md.__setitem__(8,0)
md.__len__()
md.__setitem__(5,2)
md.__setitem__(0,1)
md.clear()
md.clear()
md.__setitem__(1,3)
md.__contains__(7)
md.__contains__(4)
md.__contains__(2)
md.__setitem__(3,0)
md.__setitem__(6,2)
md.__contains__(2)
md.__setitem__(0,8)
md.__setitem__(8,1)
md.__delitem__(0)
print(md)
print(md.__getitem__(3))