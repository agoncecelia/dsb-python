#Function with no argument and no Return value
def greet():
    print("Hello world")
greet()
#Function with no argument and with Return value
def greet_2():
    return "Hello world"
print(greet_2())
#Python Function with argument and No Return value
def greet_3(name):
    print("Hello " + name)
greet_3("Kastriot")
#Function with argument and Return value
def greet_4(name, surname):
    return "Hello " + name + " " + surname
print(greet_4("Krenar", "Voca"))
