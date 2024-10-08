import math

class Task78a:
    def __init__(self, a, n):
        self.a = a  
        self.n = n  

    def calc(self):
        return math.pow(self.a, self.n) 

a = float(input())
n = int(input())

calculator = Task78a(a, n)

res = calculator.calc()
print(f"{a}^{n} = {res}")