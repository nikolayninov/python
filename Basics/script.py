student_names = ["James", "Katarina",
                 "Jessica", "Mark", "Bort", "Frank Grimes"]


def find(search_for_name):
    found_name = None
    for name in student_names:
        if name == search_for_name:
            found_name = name
            break
    print("Found him!" if found_name else f"Couldn't find {search_for_name}")


find("Bort")


def var_args(name, *args):
    print(name)
    print(args)


var_args("Mark", "Loves", "Python")
