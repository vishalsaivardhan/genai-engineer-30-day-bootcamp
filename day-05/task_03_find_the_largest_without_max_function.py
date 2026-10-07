# Task-03 : Find largest without max()

#data
list = [1,2,3,10,4,5,5]

#process & output
data = set(list)
largest = 0
for num in data:
    if num > largest:
        largest = num
print(largest)