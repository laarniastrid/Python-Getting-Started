# functions
# print('hello world')
# str(3)  # '3'
# int('15')  # 15
# username = input('enter the user\'s name: ')

#
students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase

# # similar to get_students_titlecase function
# def print_students_title():
#     students_titlecase = []
#     for student in students:
#         students_titlecase = student.title()
#     print(print_students_title)

def print_students_titlecase():
    students_titlecase = get_students_titlecase()


def add_student(name):
    students.append(name)

student_list = get_students_titlecase()

add_student('mark')
print(students)
