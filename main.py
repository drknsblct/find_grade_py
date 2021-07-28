import sqlite3
from find_grade_functions import courses, findStudentAverage, findClassAverage

conn = sqlite3.connect(':memory:')
c = conn.cursor()

while True:
    try:
        answer = int(input("[1] Add Courses\t\t\t\t" +
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
        courses()
    elif answer == 2:
        pass
    elif answer == 3:
        pass
    elif answer == 4:
        print("\n<<< Find Average Score >>>")
        findStudentAverage()
    elif answer == 5:
        pass
    elif answer == 6:
        print("\n Find Class Average Score")
        findClassAverage()
    else:
        print("Input must be between 0 - 6!\n")
