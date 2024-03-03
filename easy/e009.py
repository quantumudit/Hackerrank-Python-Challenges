if __name__ == "__main__":
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Extract the second lowest (sl) score
    sl_score = sorted(set([score for _, score in students]))[1]

    # Extract the student names (in ascending order) with second lowest (sl) scores
    sl_students = sorted([name for name, score in students if score == sl_score])

    # Print names of students with second lowest scores
    for student_name in sl_students:
        print(student_name)
