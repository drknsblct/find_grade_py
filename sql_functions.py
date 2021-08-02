import sqlite3

# conn = sqlite3.connect('drkns.db')
conn = sqlite3.connect(':memory:')
c = conn.cursor()


def create_table(table_name):
    c.execute(f"CREATE TABLE {table_name} (Id INTEGER, Name TEXT, Grade DOUBLE, PRIMARY KEY (Id))")


def find_average(table_name):
    if table_name == 'courses':
        c.execute(f'SELECT SUM(Grade) / MAX(Id) FROM courses')
    elif table_name == 'students':
        c.execute(f'SELECT SUM(Grade) / MAX(Id) FROM students')
    data = c.fetchall()
    for row in data:
        print(f"-->Average: {''.join(str(f'{x:.2f}<--') for x in row)}\n\n")


def get_from_table(table_name):
    if table_name == 'courses':
        c.execute(f'SELECT * FROM {table_name}')
        # print("<< Courses >> ")
    elif table_name == 'students':
        c.execute(f'SELECT * FROM {table_name} ORDER BY grade DESC')
    data = c.fetchall()
    for row in data:
        print(' '.join(str(x) for x in row))


def update_grade(student):
    with conn:
        c.execute('UPDATE students SET Grade = ? WHERE Name = ?',
                  (f'{student.get_grade() / 6:.2f}', student.get_name()))


def remove_from_table(table_name, id):
    with conn:
        c.execute(f'DELETE from {table_name} WHERE id = ?', (id,))


def insert_to_table(table_name, obj):
    with conn:
        c.execute(f'INSERT INTO {table_name} (Name, Grade) VALUES(?, ?)', (obj.get_name(), obj.get_grade()))
