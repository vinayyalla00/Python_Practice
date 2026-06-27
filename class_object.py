
class student:

    def __init__(self, name, roll, gpa):
         self.name = name;
         self.roll = roll;
         self.gpa = gpa
    

    def display(self):
         print("Name:", self.name);
         print("Roll:", self.roll)
         print("GPA:", self.gpa);


s1 = student("Vinay", 101, 3.0)

s1.display();


