class Person:
    def __init__(self, name, surname, birthdate, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.email = email

    def get_email(self):
        return self.email

class Student(Person):
    def __init__(self, name, surname, birthdate, email, student_id, grade_average):
       super().__init__(name, surname, birthdate, email)
       self.student_id = student_id
       self.grade_average = grade_average

    def get_average(self):
        return self.grade_average

class Staff(Person):
    def __init__(self, name, surname, birthdate, email, auth_id, role, exp_date):
       super().__init__(name, surname, birthdate, email)
       self.auth_id = auth_id
       self.role = role
       self.exp_date = exp_date

    def get_role(self):
        return self.role


agoni = Staff("Agon", "Cecelia", "19051993", "agonn.c@gmail.com", "10001032", "teacher", "01012022")

print(agoni.name)
print(agoni.get_role())
 
driloni = Student("Drilon", "Ibrahimi", "10111995", "drilon@gmail.com", "10001035", 9.2)
print(driloni.name)
print(driloni.get_average())
print(driloni.get_email())
