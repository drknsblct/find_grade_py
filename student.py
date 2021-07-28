class Student:

    def __init__(self, name=None, grade=0):
        self.name = name
        self.grade = grade

    def addGrade(self, grade):
        self.grade += grade

    def getGrade(self):
        return self.grade

    def getName(self):
        return self.name
