import sqlite3

# conn = sqlite3.connect('drkns.db')
conn = sqlite3.connect(':memory:')
c = conn.cursor()


def create_table(tableName):
    c.execute(f"CREATE TABLE {tableName} (Id INTEGER, Name TEXT, Grade DOUBLE, PRIMARY KEY (Id))")


def find_average(tableName):
    if tableName == 'courses':
        c.execute(f"SELECT SUM(Grade) / MAX(Id) FROM courses")
    elif tableName == 'students':
        c.execute(f"SELECT SUM(Grade) / MAX(Id) FROM students")
    data = c.fetchall()
    for row in data:
        print(f"-->Average: {''.join(str(f'{x:.2f}<--') for x in row)}\n\n")


def get_from_table(tableName):
    if tableName == "courses":
        c.execute(f"SELECT * FROM {tableName}")
        # print("<< Courses >> ")
    elif tableName == 'students':
        c.execute(f"SELECT * FROM {tableName} ORDER BY grade DESC")
    data = c.fetchall()
    for row in data:
        print(' '.join(str(x) for x in row))


def update_grade(student):
    with conn:
        c.execute("UPDATE students SET Grade = ? WHERE Name = ?",
                  (f'{student.getGrade() / 6:.2f}', student.getName()))


def remove_from_table(tableName, id):
    with conn:
        c.execute(f"DELETE from {tableName} WHERE id = ?", (id,))


def insert_to_table(tableName, varObj):
    with conn:
        c.execute(f"INSERT INTO {tableName} (Name, Grade) VALUES(?, ?)", (varObj.getName(), varObj.getGrade()))
