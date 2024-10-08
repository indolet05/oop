class Animal:
    def __init__(self, age, weight, name, family):
        self.age = age
        self.weight = weight
        self.name = name
        self.family = family

        self.__money = 0  # Инициализация денег
        self.__presents = []  # Инициализация списка подарков
        print("CONSTRUCTOR WAS CALLED")

    def get_age(self):
        return self.age
    
    def celebrate_birthday(self, money, present: dict):
        self.__money += money  # Увеличение суммы денег
        self.__presents.append(present)  # Добавление подарка

        self.age += 1  # Увеличение возраста

        return self.age

    def get_money_and_presents(self):
        return self.__money, self.__presents  # Возврат денег и списка подарков


class Dog(Animal):
    def __init__(self, age, weight, name, family, breed):
        super().__init__(age, weight, name, family)  # Вызов конструктора Animal
        self.breed = breed  # Добавляем атрибут породы

    def celebrate_birthday(self, money, present: list, special):
        self._Animal__money += money  # Обновление приватного атрибута __money
        self._Animal__presents.append(present)  # Обновление списка подарков
        self.special = special  # Новый атрибут "special"

        self.age += 1  # Увеличение возраста

        return self.age


# Создание объекта Dog
dog = Dog(15, 10, "Kari", "Canine", "Tobet")

# Проверка возраста собаки
print(f"Initial age: {dog.get_age()}")  # Выведет: Initial age: 15

# Отметим день рождения собаки
dog.celebrate_birthday(200, ["Bone"], "Special treat")

# Проверка возраста после дня рождения
print(f"Age after birthday: {dog.get_age()}")  # Выведет: Age after birthday: 16

# Проверка суммы денег и списка подарков
money, presents = dog.get_money_and_presents()
print(f"Money: {money}, Presents: {presents}")  # Выведет: Money: 200, Presents: [['Bone']]

