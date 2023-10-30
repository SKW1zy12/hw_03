import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students
                  (id INTEGER PRIMARY KEY, name TEXT, surname TEXT, birth_date TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS courses
                  (id INTEGER PRIMARY KEY, name TEXT, teacher TEXT)''')

class Student:
    def __init__(self, id, name, surname, birth_date):
        self.id = id
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.courses = []

    def add_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"{self.name} {self.surname} был добавлен на курс {course_name}")

    def save_to_database(self):
        cursor.execute("INSERT INTO students (name, surname, birth_date) VALUES (?, ?, ?)",
                       (self.name, self.surname, self.birth_date))
        conn.commit()

    @staticmethod
    def get_courses_by_student(name, surname):
        cursor.execute("SELECT courses.name FROM courses "
                       "JOIN students ON courses.id = students.id "
                       "WHERE students.name = ? AND students.surname = ?", (name, surname))
        return [row[0] for row in cursor.fetchall()]

class Course:
    def __init__(self, id, name, teacher):
        self.id = id
        self.name = name
        self.teacher = teacher

    def save_to_database(self):
        cursor.execute("INSERT INTO courses (name, teacher) VALUES (?, ?)",
                       (self.name, self.teacher))
        conn.commit()

    @staticmethod
    def get_students_by_course(course_name):
        cursor.execute("SELECT students.name, students.surname FROM students "
                       "JOIN courses ON students.id = courses.id "
                       "WHERE courses.name = ?", (course_name,))
        return [f"{row[0]} {row[1]}" for row in cursor.fetchall()]


student1 = Student(1, "Иван", "Иванов", "01-01-2000")
student1.add_course("Математика")
student1.add_course("Физика")
student1.save_to_database()  

course1 = Course(1, "Математика", "Профессор Петров")
course1.save_to_database()  

students_in_math_course = Course.get_students_by_course("Математика")

courses_of_student1 = Student.get_courses_by_student("Иван", "Иванов")
