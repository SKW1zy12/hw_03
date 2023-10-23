import sqlite3

conn = sqlite3.connect('car_service.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY,
    brand TEXT,
    model TEXT,
    year INTEGER,
    description TEXT,
    status TEXT
    )''')

conn.commit()

def add_car(brand, model, year, description, status):
    cursor.execute('INSERT INTO cars (brand, model, year, description, status) VALUES (?, ?, ?, ?, ?)',
                   (brand, model, year, description, status))
    conn.commit()

def update_car(car_id, brand, model, year, description, status):
    cursor.execute('UPDATE cars SET brand=?, model=?, year=?, description=?, status=? WHERE id=?',
                   (brand, model, year, description, status, car_id))
    conn.commit()

def get_cars_in_service():
    cursor.execute('SELECT * FROM cars WHERE status="In Service"')
    cars = cursor.fetchall()
    return cars

def get_completed_cars():
    cursor.execute('SELECT * FROM cars WHERE status="Completed"')
    cars = cursor.fetchall()
    return cars

while True:
    print("\nМеню:")
    print("1. Добавить автомобиль на обслуживание")
    print("2. Обновить информацию об автомобиле")
    print("3. Просмотреть автомобили на обслуживании")
    print("4. Просмотреть готовые автомобили")
    print("5. Выход")
    
    choice = input("Выберите действие: ")

    if choice == "1":
        brand = input("Марка автомобиля: ")
        model = input("Модель автомобиля: ")
        year = int(input("Год выпуска: "))
        description = input("Описание работ: ")
        status = "In Service"
        add_car(brand, model, year, description, status)
        print("Автомобиль добавлен на обслуживание.")

    elif choice == "2":
        car_id = int(input("Введите номер автомобиля для обновления: "))
        brand = input("Марка автомобиля: ")
        model = input("Модель автомобиля: ")
        year = int(input("Год выпуска: "))
        description = input("Описание работ: ")
        status = input("Статус обслуживания (In Service/Completed): ")
        update_car(car_id, brand, model, year, description, status)
        print("Информация об автомобиле обновлена.")
    
    elif choice == "3":
        cars_in_service = get_cars_in_service()
        for car in cars_in_service:
            print(f"Номер: {car[0]}, Марка: {car[1]}, Модель: {car[2]}, Год выпуска: {car[3]}, Описание работ: {car[4]}")
    
    elif choice == "4":
        completed_cars = get_completed_cars()
        for car in completed_cars:
            print(f"Номер: {car[0]}, Марка: {car[1]}, Модель: {car[2]}, Год выпуска: {car[3]}, Описание работ: {car[4]}")
    
    elif choice == "5":
        conn.close()
        break

    else:
        print("Неверный выбор. Попробуйте еще раз.")
