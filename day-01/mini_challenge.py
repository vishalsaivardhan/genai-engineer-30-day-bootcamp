#challenge : create a program that asks for student name , marks in python,mathematics and computer science calculate total and average later display the output

#input
name = str(input("Entet your name : "))
python = int(input("Enter your python marks : "))
math = int(input("Enter your mathematics marks : "))
computer_science = int(input("Enter your computer science marks : "))

#process
total = python + math + computer_science
average = total / 3

#output
print("=== MARKS REPORT ====")
print("Student : ",name)
print("Python : ",python)
print("Mathematics : ",math)
print("Computer Science : ",computer_science)
print("Total : ",total)
print("Average : ",average)