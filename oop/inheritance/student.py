class Physical:

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

class Academic:

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

class Student(Physical, Academic):

    def __init__(self, name, gpa, weight, height):
        self.name = name
        self.gpa = gpa
        self.weight = weight
        self.height = height

    @property
    def bmi(self):
        return self.weight / (self.height/100) ** 2

    @property
    def is_honor(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self.name} - GPA: {self.gpa}, BMI: {self.bmi:.2f}"
    

student1 = Student("Josh", 3.7, 70, 189)
print(student1.bmi)
print(student1.is_honor)
print(student1)
