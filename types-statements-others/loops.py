# basic loops
student_names = ['mark', 'katarina', 'jessica']

for name in student_names:
    print('student name is {0}'.format(name))


# loops with range
x = 0
for index in range(10):
    x += 10
    print('the value of X is {0}'.format(x))

# loops with range not starting with 0
# 2 arguments [start, end]
for index in range(5, 10):
    print('the value iis {0}'. format(index))

for index in range(5, 10):
    index += 2
    print('the value is {0}'. format(index))


# loops with range not starting with 0
# 3 arguments [start, end, increment[
for index in range(5, 30, 3):
    print('the value is {0}'.format(index))
