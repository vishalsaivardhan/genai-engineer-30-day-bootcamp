# Task-03 : Count Vowels

#input
word = input("Enter the word : ")

#process
count = 0
word = word.lower()
for character in word :
    if character in "aeiou":
        count += 1

#output
print("Vowels : ",count)