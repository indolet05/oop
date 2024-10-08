class Task251:
    def __init__(self, s):
        self.s = s

    def calc(self):
        return self.s.count('x')

input_string = input("Введите строку символов: ")

counter = Task251(input_string)
result = counter.calc()
print(f"Буква 'x' встречается {result} раз(а).")