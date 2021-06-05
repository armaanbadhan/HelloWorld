class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def intelligent(self):
        if self.gpa >= 9:
            return True
        else:
            return False


student1 = Student("Armaan", "Maths", 9.2)
student2 = Student("Badhan", "physics", 8.2)

print(student2.intelligent())
