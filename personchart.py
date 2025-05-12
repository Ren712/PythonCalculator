from datetime import date

class Person:
    estado = "0"
    def __init__ (self, name, country, dob):
        self.name = name
        self.country = country 
        self.dob = dob

    def calculateAge(self):
        if self.estado == '0':
            print("no hay datos")
            return 0 
        today = date.today()
        age = today.year - self.dob.year
        if today < (date(today.year, self.dob.month, self.dob.day)):
            age =-1
        return age

dobyear = int(input("Ingrese su ano de nacimiento: "))
yo = Person('reni', 'arg', date(dobyear,4,3))

yo.estado = input("Ingrese 1 o 0: ")
print(yo.calculateAge())


