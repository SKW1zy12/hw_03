# class User:
#     def __init__(self, name, email, phone):
#         print(name)

#     def into(self):
#         print(self.name)


# user = User("Нурболот", "hdajdhahj@gmail.com", '0554616367')
# user.info()


# class User:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone

#     def info(self):
#         print(self.name)

# user = User("Нурболот", "hdajdhahj@gmail.com", '0554616367')
# user.info()


# class Dad:
#     def info_dad(self):
#         print("Я отец")

# class Son(Dad):
#     def info_son(self):
#         print("Я сын")

# son = Son()
# son.info_son()
# son.info_dad()


# class Dog:
#     def info_dog(self,):
#         print("Гаф, Гаф")
        

# class Cat(Dog):
#     def info_Cat(self,):
#         print("Мяу")

# cat = Cat()
# cat.info_Cat()
# cat.info_dog()


# class Mother:
#     def info_mom(self):
#         print("Я мама. Я родительский класс")

# class Father:
#     def info_dad(self):
#         print("Я папа. Я родетильский класс")
 
# class Son(Mother,Father):
#     def info_Son(self):
#         print("Я сын. Я дочерный класс Son, Я наследусь от класса  Mother и Father")

# son = Son()
# son.info_mom()
# son.info_dad()
# son.info_Son()

class Phone:
    def info_phone(self):
        print("Я звоню маме")

class Camera:
    def info_Camera(self):
        print("Я фоткаю отца")

class SmartPhone(Phone, Camera):
    def info_SmartPhone(self):
        print("Я ФОТКАЮ И так ЖЕ ЗВОНЮ")

SmartPhone = SmartPhone()
SmartPhone.info_phone()
SmartPhone.info_Camera()
SmartPhone.info_SmartPhone()

class  Dad:
    def car(self):
        print('Машина: BWM')

class Mom:
    name = "Aigul"
    def home(self):
        print('Дом')

class Son(Dad, Mom):
    def dont(self):
        print("Нечего нет")
        

son = Son()
son.car()