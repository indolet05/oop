class Pet:
    def __init__(self, name: str, age: int):
        self.__name = name 
        self.__age = age

    def set_name(self, name: str):
        self.__name = name

    def set_age(self, age: int):
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age


class Dog(Pet):
    def bark(self):
        return "Woof!"

    def make_sound(self):
        return self.bark()


class Cat(Pet):
    def meow(self):
        return "Meow!"

    def make_sound(self):
        return self.meow()


class Bird(Pet):
    def chirp(self):
        return "Chirp!"

    def make_sound(self):
        return self.chirp()


if __name__ == "__main__":
    dog = Dog("Buddy", 3)
    cat = Cat("Whiskers", 2)
    bird = Bird("Tweety", 1)

    pets = [dog, cat, bird]
    
    for pet in pets:
        print(f"{pet.get_name()} says: {pet.make_sound()}")