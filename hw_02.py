#Задача 1
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model 
        self.year = year

    def info(self):
        super().info()
        print(f"Год выпуска: {self.year}")


my_car = Car("Toyota", "Camry", 2022)
my_car.info()

#Задача 2

class Parent:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Mother(Parent):
    def __init__(self, first_name, last_name, child_count):
        self.first_name = first_name
        self.last_name = last_name
        self.child_count = child_count

    def get_child_count(self):
        return self.child_count


class Father(Parent):
    def __init__(self, first_name, last_name, child_count):
        self.first_name = first_name
        self.last_name = last_name
        self.child_count = child_count

    def get_child_count(self):
        return self.child_count

mother = Mother("Анна", "Иванова", 2)
father = Father("Иван", "Иванов", 2)

print(f"Мама: {mother.get_full_name()}, Количество детей: {mother.get_child_count()}")
print(f"Папа: {father.get_full_name()}, Количество детей: {father.get_child_count()}")