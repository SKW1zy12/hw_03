#Задача 1
class Shape:
    def draw(self):
        print("Рисуем фигуру")

class Circle(Shape):
    def draw(self):
        print("Рисуем круг")

class Rectangle(Shape):
    def draw(self):
        print("Рисуем прямоугольник")


shape = Shape()
circle = Circle()
rectangle = Rectangle()

shape.draw()     
circle.draw()     
rectangle.draw()  

#Задача 2
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self, value):
        self.value += value

    def get_value(self):
        return self.value


counter = Counter()
print(counter.get_value())  #

counter.increment(5)
print(counter.get_value())  

counter.increment(3)
print(counter.get_value())  
