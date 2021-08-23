class Student:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.courses = {}

    def get_student(self):
        return "{} {} {} {}".format(self.id, self.name, self.email, self.courses)
