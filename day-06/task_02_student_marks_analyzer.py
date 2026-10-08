# Task-02: student marks analyzer

#data
marks = {
    "Ravi": 85,
    "Arun": 72,
    "Priya": 91,
    "Anu": 68
}

#logic
highest = 0
lowest = 100
total = 0

for student, mark in marks.items():

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

    total = total + mark

average = total / len(marks)

#output
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)

print("Students above 80:")
for student, mark in marks.items():
    if mark > 80:
        print(student, mark)