# exceptions
student = {
    'name': 'mark',
    'student_id': 15163,
    'feedback': None
}

student['last_name'] = 'kowalski'

try:
    last_name = student['last_name']
    numbered_last_name = 3 + last_name
except KeyError:
    print('error finding last_name')
except TypeError as error:
    print('i can\'t add these two together!')
    print(error)
except Exception:
    print('unknown error')
finally:
    print('try exceptions completed')

print('this code executes')
