class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        print(sum(self.marks)/len(self.marks))    
 

s1 = Student('John', [45, 67, 89, 90, 78])        

s1.get_avg()