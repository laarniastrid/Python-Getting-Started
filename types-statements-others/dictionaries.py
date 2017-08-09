# dictionaries
student = {
    'name': 'mark',
    'student_id': 15163,
    'feedback': None
}

all_students = [
    {
        'name': 'mark',
        'student_id': 15163
    },
    {
        'name': 'katarina',
        'student_id': 63112
    },
    {
        'name': 'jessica',
        'student_id': 30021
    }
]

student['name'] # 'mark'
student['last_name']  # KeyError
student.get('last_name', 'unknown')  # 'unknown'

student.keys()  # ['name', 'student_id', 'feedback']
student.values()  # ['mark', 15163, None]
student['name'] = 'james'
del student['name']
