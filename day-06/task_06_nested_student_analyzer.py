# Task-06 : Nested Student Analyzer

students = [
    {
        "name": "Ravi",
        "marks": {
            "python": 85,
            "math": 90,
            "ai": 88
        }
    },
    {
        "name": "Arun",
        "marks": {
            "python": 72,
            "math": 75,
            "ai": 80
        }
    },
    {
        "name": "Priya",
        "marks": {
            "python": 91,
            "math": 95,
            "ai": 93
        }
    }
]

for student in students:

    total = 0

    for subject, mark in student["marks"].items():
        total = total + mark

    average = total / len(student["marks"])

    print("Student:", student["name"])
    print("Total:", total)
    print("Average:", average)
    print()