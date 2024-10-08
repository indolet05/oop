import math

class Task77d:
    def __init__(self, n): 
        self.n = n

    def calc(self):
        res = 0
        for i in range(self.n):  
            res = math.sqrt(2 + res)
        return res

n = int(input("n="))

t = Task77d(n)
res = t.calc()
print(res)