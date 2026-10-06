# Task-03 : Marks Analyzer

#Data
marks = [78, 92, 65, 88, 45, 76, 95]

#process and output
print("Total marks : ",sum(marks))
print("Average : ",sum(marks)/len(marks))
print("Highest mark : ",max(marks))
print("Lowest marks : ",min(marks))
count = 0
for i in marks:
    if i >= 75:
        count += 1
print("Number of students who scored >= 75 : ",count)