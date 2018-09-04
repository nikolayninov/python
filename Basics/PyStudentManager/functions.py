
def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception as error:
        print("Could not save file.")
        print(error)


read_file()
print_students_titlecase()

while True:
    add_new_student_question = input("Do you want to add a new student?")

    if add_new_student_question == "y":
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")

        add_student(student_name, student_id)
        save_file(student_name)
    elif add_new_student_question == "n":
        print_students_titlecase()
        break
