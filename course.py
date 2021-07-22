class Course:

    def __init__(self, grade, percent):
        self.grade = grade
        self.percent = percent

    def modifyGrade(self):
        return self.grade * (self.percent / 100)
       