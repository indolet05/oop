class Task82:
    def __init__(self, x):
        self.x = x  

    def calc(self):
        numerator_factors = [2, 4, 8, 16, 32, 64]
        numerator = 1
        for factor in numerator_factors:
            numerator *= (self.x - factor)

        denominator_factors = [1, 3, 7, 15, 31, 63]
        denominator = 1
        for factor in denominator_factors:
            denominator *= (self.x - factor)
            
        return numerator / denominator

x = float(input())

calculator = Task82(x)

res = calculator.calc()
print(f"Результат выражения для x = {x}: {res}")
