from course import Course
from sql_functions import *
from student import Student


def courses():
    course = None
    courses = []
    numOfCourses = int(input("Enter number of courses: "))

    for i in range(numOfCourses):
        courseName = input(f"\nEnter name of course[{i+1}]: ")
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
        insert_to_table("courses", c)
    print()
    get_from_table("courses")
    print()
    find_average("courses")


def findStudentAverage():
    sum = 0
    for i in range(1, 7):
        grade = int(input(f'Enter grade[{i}]: '))
        sum += grade

    print(f'\nGrade: {sum / 6:.2f}')


def findClassAverage():
    students = []

    loops = int(input("How many students? "))
    print()

    for i in range(loops):
        name = input(f"Name[{i+1}]: ")
        students.append(Student(name))

    # print()

    for i in range(1, 7):
        print()
        for j in range(len(students)):
            grade = int(input(f'Course[{i}], {students[j].getName()}: '))
            students[j].addGrade(grade)

    for st in students:
        insert_to_table("students", st)
        update_grade(st)

    print()
    get_from_table("students")
    print()
    find_average("students")

