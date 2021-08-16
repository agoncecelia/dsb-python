"""Me kriju nje klase staf qe permbane id, emrin mbiemrin dhe prezencen.
Me kriju nje program i cili ka mundesi me shtu nje staf te ri ne databaze (memorie) dhe me ja vendose prezencen si True. Gjithashtu ne program mundet me u pa se kush eshte prezent. """

class Staff:
    def __init__(self, name, surname, id, present):
        self.name = name
        self.surname = surname
        self.id = id
        self.present = present

    def get_staff(self):
        p = "not present"
        if self.present:
            p = "present"
        return "{} {} with id: {} is {}".format(self.name, self.surname, self.id, p)

    def set_presence(self):
       self.present = True
       return "{} {} with id: {} joined class". format(self.name, self.surname, self.id)

staff = []
inp = ""
while inp != 'q':
    inp = input("Press a to add student, l to list students, q to quit, p for presence: ")
    if inp == 'a':
        name = input("Write student name: ")
        surname = input("Write student surname: ")
        id = input("Write student id: ")
        present = False
        s = Staff(name, surname, id, present)
        staff.append(s)
    if inp == 'l':
        for x in staff:
            print(x.get_staff())
    if inp == 'p':
        inp = input("Write user id: ")
        for x in staff:
            if x.id == inp:
                print(x.set_presence())


