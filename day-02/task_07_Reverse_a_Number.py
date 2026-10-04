# Task-07 : Reverse a number

#input
number = int(input("Enter the number : "))

#logic
reverse = 0
while number >0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

#output
print("reversed number is : ",reverse)