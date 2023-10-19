class Animal:
    def __init__(self, name, age):
        self._name = name  
        self._age = age    

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age) 
        self._breed = breed 

    def bark(self):
        print(f"{self._name} лает: Gaf, Gaf!")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)  
        self._color = color 

    def meow(self):
        print(f"{self._name} мяукает: Meow, meow!")

dog = Dog("Рекс", 3, "Бульдог")
cat = Cat("Мурка", 2, "Серый")

print(f"{dog.get_name()} - возраст {dog.get_age()} года, порода {dog._breed}")
dog.bark()

print(f"{cat.get_name()} - возраст {cat.get_age()} года, цвет {cat._color}")
cat.meow()
