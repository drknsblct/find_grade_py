class Courses:

    def __init__(self):
        self.courseMap = {}

    def addCourseAndGrade(self, course, grade):
        self.courseMap[course] = grade

    def size(self):
        return len(self.courseMap)

    def returnCourses(self):
        sum = 0

        for name, num in self.courseMap.items():
            value = self.courseMap.get(name)
            sum += num
            print(f'{name}: {value:.2f}')
            print(f'-->Average: {sum / len(self.courseMap):.2f}<--')

    def contains(self, name):
        return name in self.courseMap

    def remove(self, course):
        self.courseMap.pop(course)

    def clear(self):
        self.courseMap.clear()










