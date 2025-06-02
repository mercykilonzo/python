
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("woff!")

class Cat(Animal):
    def make_sound(self):
        print("moew!")       


class Account:
    def __init__(self,name):
        self._balance = 0
                         