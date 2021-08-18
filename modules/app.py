from person import Person
from worker import Worker

list = []
inp = ''
while inp != 'q':
    inp = input("Press a to add new worker or person, press l to list, press d to delete: ")
    if inp == 'a':
        inp = input("Press p to add person and w to add worker: ")
        if inp == 'p':
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            email = input("Enter email: ")
            list.append(Person(email, name, surname))
        if inp == 'w':
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            email = input("Enter email: ")
            profession = input("Enter profession: ")
            years_of_exp = input("Enter years of exp: ")
            list.append(Worker(email, name, surname, profession, years_of_exp))
    if inp == 'l':
        for x in list:
            print("{} {} {}".format(x.name, x.lastname, x.email))
    if inp == 'd':
        inp = input("Enter email to delete: ")
        counter = 0
        for x in list:
            if inp == x.get_email():
                list.pop(counter)
            counter += 1