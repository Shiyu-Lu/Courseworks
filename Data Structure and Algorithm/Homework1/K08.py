# basic functions

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        s = ''
        if self:
            s = '['+str(self.getRootVal())+','
            if self.getLeftChild():
                s += str(self.getLeftChild())
            else:
                s += '[]'
            s += ','
            if self.getRightChild():
                s += str(self.getRightChild())
            else:
                s += '[]'
                s += ']'
        return s

    def height(self):
        rh = lh = 0
        if self.getLeftChild():
            lh = self.getLeftChild().height()
        if self.getRightChild():
            rh = self.getRightChild().height()
        return 1+max(lh,rh)

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getRootVal(self):
        return self.key

    def setRootVal(self,obj):
        self.key = obj

# build a tree

def buildTree():
    r = BinaryTree('a')
    r.insertLeft('b')
    r.getLeftChild().insertRight('d')
    r.insertRight('c')
    r.getRightChild().insertLeft('e')
    r.getRightChild().insertRight('f')
    return r

print(buildTree())
print(buildTree().height())
