class Task334a:
    def __init__(self, s):
        self.s = s

    def count_symbols(self):
        count_plus = self.s.count('+')
        count_star = self.s.count('*')
        count_minus = self.s.count('-')
        total_count = count_plus + count_minus + count_star
        
        return count_plus, count_star, total_count

n = int(input("Введите количество символов: "))
input_string = input("Введите строку символов: ")

counter = Task334a(input_string)
plus_count, star_count, total_count = counter.count_symbols()

print(f"Символ '+' встречается {plus_count} раз(а).")
print(f"Символ '*' встречается {star_count} раз(а).")
print(f"Общее число вхождений символов +, -, *: {total_count}.")