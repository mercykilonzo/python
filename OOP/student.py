
# class Student:
#     name = "Kisanat"
#     age = 21
#     school = "AkiraChix"
#     country = "Ethiopia"

class Student:
    school = "AkiraChix"
    def __init__(self,firstname,lastname,age,country):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.year = 2025 - age
        self.marks = []
    def great_student(self):
        return f"Hello {self.name}, welcome to {self.school}."    
    def initials(self):
        x = self.firstname[0].upper()
        y = self.lastname[0].upper()
        return x+y
    def record_marks(self,mark):
        self.marks.append(mark)
        total = 0
        for mark in self.marks:
            total+=mark
        return f"Marks recorded. Total marks is {total}"   

        





