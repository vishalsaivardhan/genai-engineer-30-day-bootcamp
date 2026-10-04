# Task-06 : Count Digit

#input
number = int(input("Enter the number : "))

#logic
count = 0
while number > 0:
    number = number // 10
    count = count + 1

#output    
print("number of digits:",count)