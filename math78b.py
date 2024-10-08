import math

class Task78b:
    def __init__(self, a, n):
        self.a = a
        self.n = n

    def calc(self):
        result = 0
        for i in range(self,n):
            result += a + i
            return result
        a = int(input())
        n = int(input())

        calculator = Task78b(a,n)
        res = calculator.calc()
        print(f"Сумма чисел от {a} до {a + n - 1} = {res}")