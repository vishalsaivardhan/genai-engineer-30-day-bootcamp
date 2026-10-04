# Task-02 : Largest of three numbers

#input
number_1 = int(input("Enter the first number : "))
number_2 = int(input("Enter the second number : "))
number_3 = int(input("Enter the third number : "))

#Process
if number_1 > number_2 and number_1 > number_3:
    largest = number_1
elif number_2 > number_1 and number_2 > number_3:
    largest = number_2
else:
    largest = number_3

#output
print("the largest number is : ",largest)