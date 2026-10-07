# Task-06 : Find Second Largest

# Data
numbers = [10, 45, 23, 89, 67, 34]

# Initialize largest and second largest
if numbers[0] > numbers[1]:
    largest = numbers[0]
    second_largest = numbers[1]
else:
    largest = numbers[1]
    second_largest = numbers[0]

# Process
for num in numbers[2:]:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest:
        second_largest = num

# Output
print("Second largest:", second_largest)