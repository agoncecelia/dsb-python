class Person:
    def __init__(self, email, name, lastname):
        self.email = email
        self.name = name
        self.lastname = lastname
    
    def sleep(self):
        return "{} is sleeping".format(self.name)
    
    def eat(self):
        return "{} is eating".format(self.name)
    
    def walk(self):
        return "{} is walking".format(self.name)