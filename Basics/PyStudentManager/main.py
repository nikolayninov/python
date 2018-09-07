from student import *

read_file()
print_students_names()

while True:
    add_new_student_question = input("Do you want to add a new student?")

    if add_new_student_question == "y":
        student_name = input("Enter student's name: ")
        student_last_name = input("Enter student's last name: ")
        student_id = input("Enter student's ID: ")

        add_student(Student(student_name, student_last_name, student_id))
        save_file(Student(student_name, student_last_name, student_id))
    elif add_new_student_question == "n":
        print_students_names()
        break
