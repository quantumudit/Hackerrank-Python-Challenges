from collections import namedtuple

n_students = int(input())
cols = input().split()

Student = namedtuple("Student", " ".join(cols))

all_students = []

for _ in range(n_students):
    vals = input().split()
    student_dict = {col.strip(): val.strip() for col, val in zip(cols, vals)}
    all_students.append(Student(**student_dict))

marks = [int(item.MARKS) for item in all_students]

print(sum(marks) / n_students)
