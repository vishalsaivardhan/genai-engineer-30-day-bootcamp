# Task-04 : Simple Interest
#formula for simple interest = (P * R * T)/100

#input
Principle = float(input("Enter the principle amount: "))
Rate = float(input("Enter the rate : "))
Time = float(input("Enter the time : "))

#process
Interest = (Principle * Rate * Time) / 100

#output
print("the simple interest is : ",Interest)