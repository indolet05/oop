class Stack:
    def __init__(self):
        self.items = []  

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack") 

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack") 

    def size(self):
        return len(self.items)

s = Stack()
print(s.isEmpty())

s.push(4)
s.push('dog')
print(s.peek()) 

s.push(True)
print(s.size())  

print(s.isEmpty())

s.push(8.4)
print(s.pop())  
print(s.pop())  
print(s.size())  