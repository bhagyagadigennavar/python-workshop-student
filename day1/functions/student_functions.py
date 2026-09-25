# Day 1 - Python Fundamentals

# student_name = input("Enter student name:")
# marks_python = float(input("Enter marks for Python:"))
# marks_math = float(input("Enter marks for Mathematics:"))
# marks_comm = float(input("Enter marks for Communication:"))

# #TODO:
# #Create a function to calculate the percentage
# def calculate_percentage():
#     total = (marks_python+marks_math+marks_comm)
#     percentage = (total/3)*100
#     return percentage

# print("\n -- Result --")
# print("Student:", student_name)
# print("Percentage",calculate_percentage())


 





def input_student():
    student_name = input('enter student name:')
    marks_python = float(input("enter marks for python:"))
    marks_math = float(input("enter marks for mathematics:"))
    marks_comm = float(input("enter marks for communication:"))
    dict_student_info = {
        "name":student_name,
        "python_marks":marks_python,
        "math_marks":marks_math,
        "comm_marks":marks_comm
    }
    return dict_student_info

#TODO:
def calculate_percentage(marks_python,marks_math,marks_comm):
    total = (marks_comm+marks_math+marks_python)
    percentage=(total/300)*100
    return percentage

if __name__ == "__main__":
    print("\n -- Result --")
    student_info = input_student()

    print(student_info)
    print("student:", student_info["name"])