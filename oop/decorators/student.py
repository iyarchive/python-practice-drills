class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @classmethod
    def from_string(cls, student_string):
        name, grade = student_string.split("-")
        return cls (name, int(grade))
    
    @staticmethod
    def is_passing(grade):
        return grade >= 75
    
    def __str__(self):
        return f"{self.name} - {self.grade}"
    
jacob = Student("Jacob T. Harold", 95)

student2 = Student.from_string("Iya-95")
print(student2)

print(Student.is_passing(80))

print(jacob)
