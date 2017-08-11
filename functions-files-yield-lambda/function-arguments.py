# function arguments
students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

# student_id plus = makes it optional since it has the default value
def add_student(name, student_id=332):
    student = {'name': name, 'student_id': student_id}
    students.append(student)

def var_args(name, **kwargs):
    print(name)
    print(kwargs['description'], kwargs['feedback'])

# print(name) # error 'unresolved reference'

student_list = get_students_titlecase()

# with param inserted of 15, 332 will be overridden
add_student(name='mark', student_id=15)

# variable # arguments
# print('hello', 'world', 3, None, 'something')
var_args('mark', description='loves python', feedback=None, pluralsight_subscriber=True)
