# adding students to our app
students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student['name'].title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

# student_id plus = makes it optional since it has the default value
def add_student(name, student_id=332):
    # object property/key must have quotes
    student = {'name': name, 'student_id': student_id}
    students.append(student)


student_list = get_students_titlecase()

student_name = input('enter student name : ')
student_id = input('enter student id : ')

add_student(student_name, student_id)
print_students_titlecase()
