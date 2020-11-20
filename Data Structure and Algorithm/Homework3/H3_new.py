# ======= 1 中缀表达式求值 =======
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def calculate(s) -> float:
    # 记录操作符优先级
    prec = {}
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    # 建立空栈并解析表达式到单词列表
    opStack = Stack()
    operandStack = Stack()
    tokenList = s.split()

    # 辅助函数doMath，返回两个数经操作后的值
    def doMath(op,op1,op2):   
        if op == '^':
            return op1 ** op2
        elif op == '*':
            return op1 * op2
        elif op == '/':
            return op1 / op2
        elif op == '+':
            return op1 + op2
        elif op == '-':
            return op1 - op2

    # 输入一个操作符，从操作栈中弹出两个数，经操作后再压入栈中
    def doOperand(op):
        operand2 = operandStack.pop()
        operand1 = operandStack.pop()
        result = doMath(op,operand1,operand2) 
        operandStack.push(result)

    for token in tokenList:
        if token not in '()+-*/^':   # 操作数入操作数栈
            operandStack.push(float(token))
        elif token == '(':   # 左括号入操作符栈
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':   # 取下一个操作符做计算直到取出左括号
                doOperand(topToken)
                topToken = opStack.pop()
        else:
            # 按照优先级对操作数做计算
            while (not opStack.isEmpty()) and \
                (prec[opStack.peek()] >= prec[token]):
                topToken = opStack.pop()
                doOperand(topToken)
            opStack.push(token)
        
    # 对剩下的操作数依次进行计算
    while not opStack.isEmpty():
            topToken = opStack.pop()
            doOperand(topToken)

    # 返回最终值
    return operandStack.pop()


# ======= 2 基数排序 =======
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def radix_sort(s) -> list:
    main = Queue()
    # 将所有数压入main队列，尚未排序
    for n in s:
        main.enqueue(n)
    
    # 计算队列中最大数的位数
    d = len(str(max(s)))
    dstr = '%%0%dd' % d

    # 生成10个队列
    nums = [Queue() for _ in range(10)]

    for i in range(-1,-d-1,-1):   # 从个位开始排序至最高位 

        # 按照该位数的数值压入各栈
        while not main.isEmpty():
            n = main.dequeue()
            dn = (dstr % n)[i]
            nums[int(dn)].enqueue(n)

        # 按照先进先出原则从各栈弹出数字，压入主栈
        for k in range(10):
            while not nums[k].isEmpty():
                main.enqueue(nums[k].dequeue())

    # 用列表输出排序后的基数
    result = []
    while not main.isEmpty():
        result.append(main.dequeue())
    return result


# ======= 3 HTML标记匹配 =======
def HTMLMatch(s) -> bool:
    # 请在此编写你的代码（可删除pass语句）
    import re
    # 分隔字符串，存入列表
    char_list = list(re.split('[< ]',s))
    charStack = Stack()

    # 利用栈LIFO的原则进行匹配
    for char in char_list:

        # 若分隔后的字符串不以'/'开头，则不予匹配，压入栈中
        if ('>' in char) and (char[0] != '/'):
            charStack.push(char)
        
        # 若分隔后的字符以'/'开头，则从栈中逐步弹出字符串进行匹配
        elif ('>' in char) and char[0] == '/':
            if not charStack.isEmpty():
                head = charStack.pop()
                if  char[1:] in head or char[1:] == head: # 匹配成功
                    continue
            else:
                return False # 若栈中字符串全部不能匹配，则匹配失败

    # 若栈中没有剩余字符串，则匹配成否；否则失败
    return charStack.isEmpty()


class Node():
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrev(self, newprev):
        self.prev = newprev


# ======== 4 链表实现栈和队列 ========
# 用链表实现ADT Stack与ADT Queue的所有接口
class LinkStack():
    # 请在此编写你的代码（可删除pass语句）
    def  __init__(self):
        self.head = Node()
        self.len = 0
    
    def isEmpty(self):
        return self.len == 0
    
    def push(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.len += 1

    def pop(self):
        current = self.head
        self.head = current.getNext()
        self.len -= 1
        return current.getData()
    
    def peek(self):
        return self.head.getData()
    
    def size(self):
        return self.len
    # 代码结束


class LinkQueue():
    # 请在此编写你的代码（可删除pass语句）
    def  __init__(self):
        self.head = Node()
        self.len = 0
    
    def isEmpty(self):
        return self.len == 0
    
    def enqueue(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.len += 1

    def dequeue(self):
        current = self.head
        previous = None
        count = self.len
        if count == 1:
            d_val = current
            self.head = Node()
        else:
            while count != 2:
                count -= 1
                previous = current
                current = current.getNext()
            d_val = current.getNext()
            current.setNext(None)
        self.len -= 1
        return d_val.getData()
    
    def size(self):
        return self.len
    # 代码结束

# ======== 5 双链无序表 ========
class DoublyLinkedList():
    # 请在此编写你的代码（可删除pass语句）
    def  __init__(self,iterable=None):
        self.head = Node()
        self.tail = Node()
        self.len = 0
        if iterable != None:
            for item in iterable:
                self.append(item)
    
    def isEmpty(self):
        return self.len == 0
    
    def size(self):
        return self.len
    __len__ = size
    
    def getTail(self):
        return self.tail

    def add(self,item):
        temp = Node(item)
        if self.len == 0:
            self.head = temp
            self.tail = temp
        else:
            self.head.setPrev(temp)
            temp.setNext(self.head)
            self.head = temp
        self.len += 1

    def append(self,item):
        temp = Node(item)
        if self.len == 0:
            self.head = temp
            self.tail = temp
        else:
            self.tail.setNext(temp)
            temp.setPrev(self.tail)
            self.tail = temp
        self.len += 1

    def insert(self,idx,item):
        current = self.head
        n = 0
        while n < idx:
            current = current.getNext()
            n += 1
        
        if current is None:
            if self.head is None:
                self.add(item)
            else:
                self.append(item)
        else:
            idx = Node(item)
            idx.setNext(current)
            idx.setPrev(current.getPrev())
            if idx.getPrev() is not None:
                idx.getPrev().setNext(idx)
            current.setPrev(idx)

        self.len += 1

    def index(self,item):
        current = self.head
        n = 0
        while current is not None:
            if current.getData() == item:
                break
            current = current.getNext()
            n += 1
        else:
            return None
        return n
    
    def search(self,item):
        return self.index(item) is not None

    def delete(self,current):
        if self.head == current:
            self.head = current.getNext()
        if self.tail == current:
            self.tail = current.getPrev()
        if current.getPrev() is not None:
            current.getPrev().setNext(current.getNext())
        if current.getNext() is not None:
            current.getNext().setPrev(current.getPrev())
        self.len -= 1

    def remove(self,item):
        current = self.head
        while current is not None:
            if current.getData() == item:
                self.delete(current)
                break
            current = current.getNext()
    
    def pop(self,n=None):
        if n is None:
            n = self.len-1
        current = self.head
        i = 0
        while i<n:
            current = current.getNext()
            i+=1
        dat = current.getData()
        self.delete(current)
        return dat

    def __str__(self):
        tlist = []
        current = self.head
        while current is not None:
            tlist.append(current.getData())
            current = current.getNext()
        return str(tlist)
    __repr__ = __str__

    def __getitem__(self,key):
        if isinstance(key,int):
            current = self.head
            i = 0
            while i<key:
                current = current.getNext()
                i += 1
            if current is not None:
                return current.getData()
            else:
                raise StopIteration
        elif isinstance(key,slice):
            start = 0 if key.start is None else key.start
            stop = self.len if key.stop is None else key.stop
            step = 1 if key.step is None else key.step   

            if step > 0:
                # 对start进行处理
                start = max(start,-self.len)
                if start < 0:
                    start += self.len
                elif start > self.len - 1:
                    return DoublyLinkedList()
                #对stop进行处理
                if stop <= -self.len or stop == 0:
                    return DoublyLinkedList()
                elif stop > -self.len and stop < 0:
                    stop += self.len
                elif stop > self.len - 1:
                    stop = self.len

                current, i = self.head, 0
                while i<start:
                    current = current.getNext()
                    i += 1
                dcopy = DoublyLinkedList()
                while i<stop:
                    if current is None:
                        break
                    dcopy.append(current.getData())
                    s = step
                    while current is not None and s >0:
                        current = current.getNext()
                        s -= 1
                    i += step

            elif step < 0:
                # 对start进行处理
                if start < -self.len:
                    return DoublyLinkedList()
                elif start >= -self.len and start < 0:
                    start += self.len
                else:
                    start = min(self.len-1,start)
                #对stop进行处理
                if stop < -self.len:
                    stop = -1
                elif stop >= -self.len and stop < -1:
                    stop += self.len
                elif stop == -1 or stop >= self.len - 1:
                    return DoublyLinkedList()

                current, i = self.tail, self.len - 1
                self.head.setPrev(None)
                while i>start:
                    current = current.getPrev()
                    i -= 1
                dcopy = DoublyLinkedList()
                while i>stop and current is not None:
                    dcopy.append(current.getData())
                    s = step
                    while current is not None and s < 0:
                        current = current.getPrev()
                        s += 1
                    i += step
                    
            return dcopy
    
    def __eq__(self,other):
        if other is None or not isinstance(other,DoublyLinkedList):
            return False
        if len(self) != len(other):
            return False
        for s,o in zip(self,other):
            if s != o:
                return False
        else:
            return True