from person import Person
from worker import Worker

agoni = Person("agon@gmail.com", "Agon", "Cecelia")
rezultati = agoni.sleep()
print(rezultati)
print(agoni.walk())

gresa = Worker("gresa@gmail.com", "Gresa", "Sylejmani", "Data Scientist", 2)
print(gresa.work())
print(gresa.eat())