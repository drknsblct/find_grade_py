from find_grade_functions import *
from sql_functions import *

while True:
    try:
        answer = int(input("\n" +
                           "[1] Add Courses\t\t\t" +
                           "[4] Find Student Grade\n" +
                           "[2] View List (Databases)\t" +
                           "[5] Delete Entries\n" +
                           "[3] Reset List (Database)\t" +
                           "[6] Find Classroom Average\n" +
                           "[0] Exit\n\n" +
                           "Enter answer: "))
    except Exception:
        continue

    if answer == 0:
        print("Exiting program!\n")

    elif answer == 1:
        print("\n<<< Add Courses >>>")
        create_table("courses")
        courses()
        # conn.close()

    elif answer == 2:
        get_from_table('students')
        get_from_table('courses')
        print()
        # try/except an dn exoun ftiaxtei akoma

    elif answer == 3:
        pass

    elif answer == 4:
        print("\n<<< Find Average Score >>>")
        findStudentAverage()

    elif answer == 5:
        pass

    elif answer == 6:
        print("\n<<< Find Class Average Score >>>")
        create_table("students")
        findClassAverage()
        # conn.close()

    else:
        print("Input must be between 0 - 6!\n")
