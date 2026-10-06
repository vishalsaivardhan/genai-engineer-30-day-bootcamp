# Task-02 : Even Number Extractor

#list
numbers = [12, 7, 9, 20, 33, 44, 51, 60]

#process and output
Even = []
for number in numbers:
    if number % 2 == 0:
        Even.append(number)
print(Even)