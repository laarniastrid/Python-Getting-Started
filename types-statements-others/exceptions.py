# exceptions
student = {
    'name': 'mark',
    'student_id': 15163,
    'feedback': None
}

try:
    last_name = student['last_name']
except KeyError:
    print('error finding last_name')

print('this code executes')
