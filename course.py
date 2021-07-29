class Course:

    def __init__(self, name=None, grade=0):
        self.name = name
        self.grade = grade

    # def modifyGrade(self):
    #     return self.grade * (self.percent / 100)

    def getGrade(self):
        return self.grade

    def getName(self):
        return self.name
