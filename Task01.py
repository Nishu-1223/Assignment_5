# Task 1: Create a Dictionary of Student Marks

students_marks = {
    "Alice": 85,
    "Nishu": 92,
    "Ayush": 78,
    "Deepak": 88,
    "Sanju": 95
}

student_name = input("Enter the student's name: ")
student_name=student_name.capitalize() # used this for case-sensitive issue
if student_name in students_marks:
    print(f"{student_name}'s marks: {students_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the database.")



