import random

class Task394a:
    def __init__(self, n):
        self.n = n
        self.matrix = self.generate_random()

    def generate_random(self):
        return [[random.randint(0, 1) for _ in range(self.n)] for _ in range(self.n)]

    def calc(self):
        zero_rows = []
        for i, row in enumerate(self.matrix):
            if all(element == 0 for element in row):
                zero_rows.append(i)
        return zero_rows

n = int(input("n="))

calculator = Task394a(n)
matrix = calculator.matrix

print("матрица:")
for row in matrix:
    print(row)

result = calculator.calc()
print({result})