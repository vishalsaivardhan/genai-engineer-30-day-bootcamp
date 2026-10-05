# Task-05 : Palindrome checker

#input
word = input("Enter the word : ")

#process and output
reverse = word[::-1]
if word == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")