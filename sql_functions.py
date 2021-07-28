import sqlite3

# conn = sqlite3.connect('courses.db')
conn = sqlite3.connect(':memory:')
c = conn.cursor()


def execute_students():
    c.execute("""CREATE TABLE students (
                Id INTEGER,
                Name TEXT,
                Grade DOUBLE,
                PRIMARY KEY (Id)
                );""")

def execute_courses():
    c.execute("""CREATE TABLE courses (
                Id INTEGER,
                Name TEXT,
                Grade DOUBLE,
                PRIMARY KEY (Id)
                );""")


def find_mo():
    c.execute("SELECT SUM(Grade) / MAX(Id) from courses")
    data = c.fetchall()
    for row in data:
        print(f"Average Score: {''.join(str(f'{x:.2f}') for x in row)}\n\n")


def get_course():
    c.execute("SELECT * FROM courses")
    data = c.fetchall()
    for row in data:
        print(' '.join(str(x) for x in row))


def insert_course(course):
    with conn:
        c.execute("INSERT INTO courses (Name, Grade) VALUES(?, ?)", (course.getName(), course.getGrade()))


def get_student():
    c.execute("SELECT * FROM students ORDER BY grade DESC")
    data = c.fetchall()
    for row in data:
        print(' '.join(str(x) for x in row))


def update_grade(student):
    with conn:
        c.execute("UPDATE students SET Grade = ? WHERE Name = ?",
                  (f'{student.getGrade() / 6:.2f}', student.getName()))


def remove_student(name):
    with conn:
        c.execute("DELETE from students WHERE Name = ?", (name,))


def insert_student(student):
    with conn:
        c.execute("INSERT INTO students (Name, Grade) VALUES(?, ?)", (student.getName(), student.getGrade()))
