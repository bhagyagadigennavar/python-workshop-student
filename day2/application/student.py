class Student:
    """Represent a student."""

    def __init__(
        self,
        name,
        age,
        python,
        mathematics,
        communication,
    ):
        self.name = name
        self.age = age
        self.python = python
        self.mathematics = mathematics
        self.communication = communication

    def calculate_percentage(self):
        """Calculate the student's percentage.
        This function defict abstraction"""
        total = self.python + self.mathematics + self.communication

        return total / 3

    def display(self):
        """Display the student's details."""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Python:", self.python)
        print("Mathematics:", self.mathematics)
        print("Communication:", self.communication)
        print("Percentage:", self.calculate_percentage())

    def grade(self):
        Percentage = self.calculate_percentage()
        if Percentage >= 85:
            print("grade = A") 
        elif Percentage >= 60:
            print("grade = B")
        elif Percentage >= 45:
            print("grade = c")
        else:
            print("grade = D")

if __name__ == "__main__":
    Student_obj1 = Student("harry",12,82,86,36)
    Student_obj1.display()
    Student_obj1.grade()
    Student_obj2 = Student("heena",23,44,11,88)
    Student_obj2.display()
    Student_obj2.grade()
    Student_obj3 = Student("apeksha",29,45,66,34)
    Student_obj3.display()
    Student_obj3.grade()
    Student_obj4 = Student("sneha",67,14,57,32)
    Student_obj4.display()
    Student_obj4.grade()
    Student_obj5 = Student("kaveri",75,23,90,45)
    Student_obj5.display()
    Student_obj5.grade()
                





