# initialising the dictionary
student_grade={}
#  add a new student
def add_student(name,grade):
    student_grade[name]=grade
    # [saleem]=100
    print(f"added{name} with a {grade}")
    # add saleem with a 100

# update a student
def update_student(name,grade):
    if name in student_grade:
        student_grade[name]=grade
        # saleem=100
        print(f"{name} with marks are update{grade}")
    else:
        print(f"{name} is not found!")

# delete a student
def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} as been successfully delete")
    else:
        print(f"{name} is not found!")

# view all student
def view_all():
    if student_grade:
        for name,grade in student_grade.items():
            print(f"{name}:{grade}")
        else:
            print("no stdent found")

def main():
    print("STUDENT GRADE MANAGEMENT SYSTEM")
    print("1.add student=")
    print("2.update student=")
    print("3.delete student=")
    print("4.view all student=")
    print("5.exit=")

    while True:
        choise=int(input("enter your choise:"))

        if choise==1:
            name=input("enter student name:")
            grade=int(input("enter student grade:"))
            add_student(name,grade)
        elif choise==2:
            name=input("enter your name")
            grade=int(input("enter your grade"))
            update_student(name,grade)
        elif choise==3:
            name=input("enter your name")
            delete_student(name)
        elif choise==4:
            view_all()
        elif choise==5:
            print("thank you")
            break
        else:
            print("in_valid input")


if __name__ == "__main__":
    main()