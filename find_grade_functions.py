from course import Course
from sql_functions import *
from student import Student


def courses():
    course = None
    courses_list = []
    num_of_courses = int(input('Enter number of courses: '))

    for i in range(num_of_courses):
        course_name = input(f'\nEnter name of course[{i+1}]: ')
        num_of_cw = int(input('Enter number of CW: '))

        for j in range(num_of_cw):
            print(f'\n{course_name} - CW[{j + 1}]')
            grade_and_percent = input('Grade, Percent: ').split(',')
            grade = int(grade_and_percent[0])
            percent = int(grade_and_percent[1])

            score = grade * (percent / 100)

            course = Course(course_name, score)
        courses_list.append(course)

    for c in courses_list:
        insert_to_table('courses', c)
    print()
    get_from_table('courses')
    print()
    find_average('courses')


def find_student_average():
    sum = 0
    for i in range(1, 7):
        grade = int(input(f'Enter grade[{i}]: '))
        sum += grade

    print(f'\nGrade: {sum / 6:.2f}')


def find_class_average():
    students = []

    loops = int(input('How many students? '))
    print()

    for i in range(loops):
        name = input(f'Name[{i+1}]: ')
        students.append(Student(name))

    # print()

    for i in range(1, 7):
        print()
        for j in range(len(students)):
            grade = int(input(f'Course[{i}], {students[j].get_name()}: '))
            students[j].add_grade(grade)

    for st in students:
        insert_to_table('students', st)
        update_grade(st)

    print()
    get_from_table('students')
    print()
    find_average('students')

