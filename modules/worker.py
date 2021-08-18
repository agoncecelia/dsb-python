from person import Person

class Worker(Person):
    def __init__(self, email, name, lastname, profession, years_of_exp):
        super().__init__(email, name, lastname)
        self.profession = profession
        self.years_of_exp = years_of_exp

    def work(self):
        return "{} is working.".format(self.name)