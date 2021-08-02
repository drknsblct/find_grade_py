class Student:

    def __init__(self, name=None, grade=0):
        self.name = name
        self.grade = grade

    def add_grade(self, grade):
        self.grade += grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return self.name
