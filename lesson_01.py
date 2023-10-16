# class Geeks:
#     name = "Natasha"
#     def my_metod(self):
#         print("Привет, это мой метод!!")

#     def hello_metod(self):
#         print(f"Я {self.name}, я поняла что это твой метод")
# geeks = Geeks()
# geeks.my_metod()
# geeks.hello_metod()

# class User:
#     def __init__(self, name, surname, age, phone):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.phone = phone

#     def info_user(self):
#         print(f"Имя: {self.name}, фамилия: {self.surname}, возраст: {self.age}, номер: {self.phone} ")

# user = User("Nurbolot",  "Erkinbaev", 17, "0554616367")
# user.info_user()


# class Car:
#     def __init__(self, brand, model, year,type_fuel):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.type_fuel = type_fuel

#     def info(self):
#         print(f"Марка: {self.brand}, Модель: {self.model}, Год: {self.year}, Топливо: {self.type_fuel}")
    
#     def cars(self):
#         print("Машина завелась")
#         n = float(0)
#         while True:
#             n += 0.5
#             if n == 20:
#                 print("Вы проехали 20км")
#             elif n == 50:
#                 print("Вы проехали 50 км")
#             elif n == 80:
#                 print("Вы проехали 80км")
#                 print("У вас мало топливо")
#             elif n == 100:
#                 print("Вы проехали 100км")
#                 print("Машина остоновлена< не осталось топливо")
#                 break
# car = Car("Tayota", "Camry 75", "2022", "Бензин") 
# car.info()    
# car.cars()       