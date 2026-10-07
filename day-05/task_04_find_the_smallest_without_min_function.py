# Task-04 : Find Smallest Without min()

#data
data = {1,-1,2,3,10,4,5,5}
data = list(data)

#process & output
smallest = data[0]
for num in data:
    if num < smallest:
        smallest = num
print(smallest)