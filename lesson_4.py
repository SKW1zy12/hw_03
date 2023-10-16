# Объектно-ориентированное программирование (ООП) 
class Animals: # Чертеж
    # __init__ - конструктор
    # атрибут - сущ
    # методы - глагол
    # self - сам объект
    def __init__(self, name, breed, color):  
        self.name = name # публичный атрибут
        self._breed = breed # Защищенный атрибут
        self.__color = color # Приватный атрибут
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, new_color):
        self.__color = new_color
    
    def info(self):
        print(f"Имя - {self.name}, Порода - {self._breed}, цвет - {self.color}")

    def sound(self):
        pass

cow = Animals("Toni", "японская корова", "Black")
print(cow._breed)
print(cow.color)

class Dog(Animals):
    def __init__(self, name, breed, color, smell): # конструктор класса Dog
        Animals.__init__(self, name, breed, color)
        # super().__init__(name, breed, color)
        self.smell = smell

    def info(self):
        print(f"Имя - {self.name}, Порода - {self.breed}, цвет - {self.color}, чувствует запах с расстояния - {self.smell} км")

    def sound(self):
        print("Гаф-Гаф")

buldog = Dog("Ak-Tosh", "Buldog", "brown", 1)
buldog.info()
buldog.sound()

class Cat(Animals):
    def __init__(self, name, breed, color, mustache): # конструктор класса Dog
        Animals.__init__(self, name, breed, color)
        # super().__init__(name, breed, color)
        self.mustache = mustache

    def info(self):
        print(f"Имя - {self.name}, Порода - {self.breed}, цвет - {self.color}, длина усиков - {self.mustache} см")

    def sound(self):
        print("Meow")

murka = Cat("Masha", "Азиатская кошка", "white", 6)
murka.info()
murka.sound()

