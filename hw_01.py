class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y

    def subtract(self, x, y):
        self.result = x - y

    def multiply(self, x, y):
        self.result = x * y

    def divide(self, x, y):
        if y != 0:
            self.result = x / y
        else:
            print("Ошибка: Деление на ноль!")

def main():
    calculator = Calculator()
    
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")
        
        choice = input("Введите номер операции (1/2/3/4/5): ")
        
        if choice == '5':
            break
        
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
        if choice == '1':
            calculator.add(num1, num2)
        elif choice == '2':
            calculator.subtract(num1, num2)
        elif choice == '3':
            calculator.multiply(num1, num2)
        elif choice == '4':
            calculator.divide(num1, num2)
        
        print("Результат: ", calculator.result)

if __name__ == "__main__":
    main()