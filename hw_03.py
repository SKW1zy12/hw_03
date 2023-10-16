import time

class Timer:
    def __init__(self, initial_time):
        self.initial_time = initial_time
        self.current_time = initial_time
        self.running = False

    def get_time(self):
        return self.current_time

    def start(self):
        if self.current_time > 0 and not self.running:
            self.running = True
            while self.current_time > 0:
                print(f"Осталось времени: {self.current_time} секунд")
                time.sleep(1)
                self.current_time -= 1
            print("Таймер завершен.")
            self.running = False

    def reset(self):
        self.current_time = self.initial_time

# Пример использования
if __name__ == "__main__":
    timer = Timer(10) 
    print("Начальное значение таймера:", timer.get_time())
    
    timer.start()  
    print("Значение таймера после запуска:", timer.get_time())
    
    timer.reset() 
    print("Значение таймера после сброса:", timer.get_time())
