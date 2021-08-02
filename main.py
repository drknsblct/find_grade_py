from find_grade_functions import *
from sql_functions import *

while True:
    try:
        answer = int(input('\n' +
                           '[1] Add Courses\t\t\t' +
                           '[4] Find Student Grade\n' +
                           '[2] View List (Databases)\t' +
                           '[5] Delete Entries\n' +
                           '[3] Reset List (Database)\t' +
                           '[6] Find Classroom Average\n' +
                           '[0] Exit\n\n' +
                           'Enter answer: '))
    except Exception:
        continue

    if answer == 0:
        print('Exiting program!\n')
        break

    elif answer == 1:
        print('\n<<< Add Courses >>>')
        create_table('courses')
        courses()
        # conn.close()

    elif answer == 2:
        try:
            get_from_table('students')
        except sqlite3.OperationalError:
            print("Students table doesn't exist yet!")
        try:
            get_from_table('courses')
        except sqlite3.OperationalError:
            print("Courses table doesn't exist yet!")
        print()

    elif answer == 3:
        pass

    elif answer == 4:
        print("\n<<< Find Average Score >>>")
        find_student_average()

    elif answer == 5:
        pass

    elif answer == 6:
        print("\n<<< Find Class Average Score >>>")
        create_table('students')
        find_class_average()
        # conn.close()

    else:
        print('Input must be between 0 - 6!\n')
