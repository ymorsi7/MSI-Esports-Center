class Student(object):
    pid = ""
    name = ""
    total_usage = None  # timedelta format
    score = None        # credit score

    def __init__(self, pid, name):
        self.name = name
        self.major = major


    def update_usage(self, elapsed):
        total_usage += elapsed

def make_student(name, major):
    student = Student(name, major)
    return student

