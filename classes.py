class Student:
    def __init__(self,Name,Division,rollno):
        self.Name = Name
        self.Divison = Division
        self.rollno = rollno

Bruce = Student("Bruce","A",5)

print(Bruce.__dict__)