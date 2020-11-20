class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items(len(self.items)-1)

    def size(self):
        return len(self.items)

def offset(symbolString):
    s = Stack()
    index = 0
    while index < len(symbolString):
        symbol = symbolString[index]
        if s.isEmpty():
            s.push(symbol)
        else:
            if symbol != s.items[-1]:
                s.push(symbol)
            else:
                s.pop()
        index += 1
    return "".join(s.items)

string = input()
print (offset(string))
        
