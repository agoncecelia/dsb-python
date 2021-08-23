from student import Student

def add_student():
    id = input("Input students id: ")
    for std in student_list:
        if std.id == id:
            print("Student already exists in db.")
            return
    name = input("Input students name: ")
    email = input("Input students email: ")
    std = Student(id, name, email)
    student_list.append(std)
    print("New student added successfully. " + std.get_student())

student_list = []
print("Press A to add student, L to list students, C to add course, G to add grades for course, Q to quit: ")
inp = ''
while inp != 'Q':
    inp = input('Next command: ')
    if inp == 'A':
        add_student()
    elif inp == 'L':
        for std in student_list:
            print(std.get_student())
    elif inp == 'C':
        id = input("Input students id for course: ")
        course = input("Input course name: ")
        for std in student_list:
            if std.id == id:
                std.courses[course] = []
                print("Course added successfully. ")
                print(std.get_student())
    elif inp == 'G':
        id = input("Input students id for course: ")
        course = input("Input course name: ")
        grade = int(input("Input grade: "))
        for std in student_list:
            if std.id == id:
                std.courses[course].append(grade)
                print("Grade added successfully.")
                print(std.get_student())
    elif inp == 'D':
        id = input("Input students id to delete: ")
        for std in student_list:
            if std.id == id:
                student_list.remove(std)
    elif inp == 'H':
        print("Press A to add student, L to list students, C to add course, G to add grades for course, Q to quit: ")
    elif inp == 'Q':
        break
    else:
        continue

