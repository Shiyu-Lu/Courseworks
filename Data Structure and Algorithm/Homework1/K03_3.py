# class Stack(object):

#     def __init__(self):
#         self.items = []

#     def push(self, data):
#         self.items.append(data)

#     def pop(self):
#         return self.items.pop()

#     def isEmpty(self):
#         return self.items == []

#     def peek(self):
#         return self.items(len(self.items)-1)

#     def size(self):
#         return len(self.items)

# def dishwashing(dishes):
#     s = Stack()
#     index = 0
#     while index < len(dishes):
#         dish = int(dishes[index])
#         order = True
#         if s.isEmpty():
#             s.push(dish)
#         else:
#             if dish == dishes[index-1] + 1:
#                 order = False
#             else:
#                 continue
    
# def dishwashing(dishes):
#     index = 0
#     while index < len(dishes):
#         order = 'Yes'
#         if int(dishes[index]) == int(dishes[index-1]) + 1:
#             order = 'No'
#             break
#         else:
#             continue
#         index +=1
#     return order

dishes = input()
index = 1
order = 'Yes'
maxdish = int(dishes[0])
while index < len(dishes):
    if int(dishes[index]) < int(dishes[index-1]) or int(dishes[index]) > maxdish:
        maxdish = max(int(dishes[index]),maxdish)
    else:
        order = 'No'
        break
    index += 1
print (order)