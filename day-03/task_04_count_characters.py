# Task-04 : Count Characters

#input
sentence = input("Enter a sentence : ")

#logic
total_characters = len(sentence)
count = 0
for space in sentence:
    if space == ' ':
        count += 1

#output:
print("Total characters : ",total_characters)
print("Number of spaces : ",count)