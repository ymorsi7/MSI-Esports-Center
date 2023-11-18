class Student(object):
    name = ""
    major = ""
    total_usage = None
    score = None    # credit score

    def __init__(self, name, major):
        self.name = name
        self.major = major

def make_student(name, major):
    student = Student(name, major)
    return student

