# functions
print('hello world')
str(3)  # '3'
int('15')  # 15
username = input('enter the user\'s name: ')

#
students = []
def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase

def print_students_title():
    get_students_titlecase = []
    for student in students:
        get_students_titlecase = student.title()
    print(print_students_title)

def add_student(name):
    students.append(name)

student_list = get_students_titlecase()
