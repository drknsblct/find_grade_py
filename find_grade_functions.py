from course import Course
from sql_functions import *
from student import Student
import sqlite3

# conn = sqlite3.connect('students.db')
conn = sqlite3.connect(':memory:')

c = conn.cursor()
# c.execute("""CREATE TABLE students (
#             Id INTEGER,
#             Name TEXT,
#             Grade DOUBLE, --INTEGER
#             PRIMARY KEY (Id)
#            );""")
#
# c.execute("""CREATE TABLE courses (
#             Id INTEGER,
#             Name TEXT,
#             Grade DOUBLE,
#             PRIMARY KEY (Id)
#             );""")


def courses():
    course = None
    courses = []
    numOfCourses = int(input("Enter number of courses: "))

    for i in range(numOfCourses):
        courseName = input("Enter name of course: ")
        numOfCW = int(input("Enter number of CW: "))

        for j in range(numOfCW):
            print(f'\n{courseName} - CW[{j + 1}]')
            grade_and_percent = input('Grade, Percent: ').split(',')
            grade = int(grade_and_percent[0])
            percent = int(grade_and_percent[1])

            score = grade * (percent / 100)

            course = Course(courseName, score)
        courses.append(course)

    for c in courses:
        insert_course(c)
    get_course()
    find_mo()

# def find_mo():
#     c.execute("SELECT SUM(Grade) / MAX(Id) from courses")
#     data = c.fetchall()
#     for row in data:
#         print(f"Average Score: {''.join(str(x) for x in row)}")


#
# def get_course():
#     c.execute("SELECT * FROM courses")
#     data = c.fetchall()
#     for row in data:
#         print(' '.join(str(x) for x in row))


# def insert_course(course):
#     with conn:
#         c.execute("INSERT INTO courses (Name, Grade) VALUES(?, ?)", (course.getName(), course.getGrade()))


# def get_student():
#     c.execute("SELECT * FROM students ORDER BY grade DESC")
#     data = c.fetchall()
#     for row in data:
#         print(' '.join(str(x) for x in row))


# def update_grade(student):
#     with conn:
#         c.execute("UPDATE students SET Grade = ? WHERE Name = ?",
#                   (f'{student.getGrade() / 6:.2f}', student.getName()))


# def remove_student(name):
#     with conn:
#         c.execute("DELETE from students WHERE name = ?", (name,))

# def insert_student(student):
#     with conn:
#         c.execute("INSERT INTO students (Name, Grade) VALUES(?, ?)", (student.getName(), student.getGrade()))


def findStudentAverage():
    sum = 0
    for i in range(1, 7):
        grade = int(input(f'Enter grade[{i}]: '))
        sum += grade

    print(f'\nGrade: {sum / 6:.2f}')


def findClassAverage():
    students = []

    loops = int(input("How many students? "))

    for i in range(loops):
        name = input("Enter name: ")
        students.append(Student(name))

    print()

    for i in range(1, 7):
        print()
        for j in range(len(students)):
            grade = int(input(f'Course[{i}], {students[j].getName()}: '))
            students[j].addGrade(grade)

    for st in students:
        insert_student(st)
        update_grade(st)

    print()
    get_student()
