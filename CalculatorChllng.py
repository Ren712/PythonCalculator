import math 

class Calcu:
    def add(nroa, nrob):
        print("Performing calculations...")
        return nroa + nrob
    
    def subs(nroa, nrob):
        print("Performing calculations...")
        return nroa + nrob

    def divide(nroa, nrob):
        print("Performing calculations...")
        return nroa / nrob

    def mult(nroa, nrob):
        print("Performing calculations...")
        return nroa * nrob


reniscalcu = Calcu
suma = reniscalcu.add(3,4)

print(suma)