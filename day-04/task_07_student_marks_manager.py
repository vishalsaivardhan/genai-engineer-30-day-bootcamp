# Task-07 - mini challenge : Student Marks Manager

#data
students = ["Ravi", "Arun", "Priya", "Anu"]
marks = [78, 85, 92, 67]

#process and output
for i in range(len(students)):
    print(students[i] ,"-", marks[i])
    
print("Highest marks : ",max(marks))
print("Lowest Marks : ",min(marks))
print("Average Marks : ",sum(marks)/len(marks))