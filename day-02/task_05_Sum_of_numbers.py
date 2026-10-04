# Task-05 : Sum of Numbers

#input
n = int(input("Enter a number : "))

#logic
total = 0
for number in range(1,n+1):
    total = total + number
print(total)