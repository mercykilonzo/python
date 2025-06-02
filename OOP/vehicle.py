
# class Vehicle:
#     def __init__(self,make,model):
#         self.make = make
#         self.model = model
#     def start(self):
#         print("The engine has started")
# class Car(Vehicle):
#     def __init__(self,make,model,color):
#         super().__init__(make,model)
#         self.color = color
#     def reverse(self):
#         print("The car is reversing")
# class Lorry(Vehicle):
#     def __init__(self,make,model,color,capacity):
#         super().__init__(make,model)
#         self.color = color
#         self.capacity = capacity
#     def unload(self):
#         print("The lorry has unloaded.")


class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def start(self):
        print("The engine has started")
class Car(Vehicle):
    def __init__(self,make,model,color):
        super().__init__(make,model)
        self.color = color
    def reverse(self):
        print("The car is reversing")           
class Lorry(Vehicle):
    def __init__(self,make,model,capacity):
        super().__init__(make,model)
        self.capacity = capacity
    def unload(self):
        print("The lorry is offloading")    