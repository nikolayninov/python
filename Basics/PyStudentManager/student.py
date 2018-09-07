students = []


class Student():
    school_name = "Springfield Elementary"

    def __init__(self, name, last_name, student_id=332):
        self.name = name
        self.last_name = last_name
        self.id = student_id

    def __str__(self):
        return "Student \nName: " + f"self.name self.last_name" + "\nID: " + str(self.id)


def get_students_names():
    students_names = []
    for student in students:
        students_names.append(student.name.title() +
                              " " + student.last_name.title())
    return students_names


def print_students_names():
    students_names = get_students_names()
    print(students_names)


def add_student(student):
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(str(student.name) + " - " + str(student.last_name) +
                " - " + str(student.id) + "\n")
        f.close()
    except Exception as error:
        print("Could not save file.")
        print(error)


def read_file():
    try:
        students[:] = []
        f = open("students.txt", "r")
        for student in f.readlines():
            st_name = student.split(" - ")[0]
            st_last_name = student.split(" - ")[1]
            st_id = student.split(" - ")[2]
            st = Student(st_name, st_last_name, st_id)
            add_student(st)
        f.close()

    except Exception as error:
        print("Could not read file.")
        print(error)
