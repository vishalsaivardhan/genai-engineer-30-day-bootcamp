# Task-08 : Student Marks Analyzer

# Data
students = ["Ravi", "Arun", "Priya", "Anu"]

marks = [
    [78, 85, 92],
    [67, 72, 81],
    [90, 88, 95],
    [65, 70, 75]
]

# Process & Output
for i in range(len(students)):
    total = 0

    for mark in marks[i]:
        total = total + mark

    average = total / len(marks[i])

    print("Student:", students[i])
    print("Marks:", marks[i][0], marks[i][1], marks[i][2])
    print("Total:", total)
    print("Average:", average)
    print()