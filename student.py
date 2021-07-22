class Student:

    def __init__(self, name=None):
        self.grade = 0
        self.name = name

    def addGrade(self, grade):
        self.grade += grade

    def getGrade(self):
        return self.grade

    def clearGrades(self):
        self.grade = 0

    def getName(self):
        return self.name

    def __str__(self):
        return f'{self.name}: \t {self.grade/6:.2f}'



