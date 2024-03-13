#Write a program where the human  class is created and the object return the addition of number
class Human():
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def perfromAddition(self,Addtion,*args):
        print ("%s performed addition of two number and result is : %f",self.name,Addtion(*args))

def add(a,b):
    sum = a+b
    return sum

obj = Human("Jeetendra","Male")
obj.perfromAddition(add,20,30)
