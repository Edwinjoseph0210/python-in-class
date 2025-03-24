class Student:
    def __init__(self):
        self.roll_number = None
        self.name = None
        self.marks = []
        self.total_marks = 0

    def readdata(self):
        self.roll_number = input("Enter Roll Number: ")
        self.name = input("Enter Name: ")
        self.marks = [int(input(f"Enter marks for subject {i+1}: ")) for i in range(3)]

    def computetotal(self):
        self.total_marks = sum(self.marks)

    def printdetails(self):
        print(f"Roll Number: {self.roll_number}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Total Marks: {self.total_marks}")

student1 = Student()
student1.readdata()
student1.computetotal()
student1.printdetails()
