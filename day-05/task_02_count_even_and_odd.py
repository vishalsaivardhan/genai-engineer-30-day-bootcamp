# Task-02 : Count Even and Odd Numbers

#data
list = [1,2,3,4,5,6]

#process and output
count_even = count_odd = 0
for num in list:
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("Number of even : ",count_even)
print("Number of odd : ",count_odd)