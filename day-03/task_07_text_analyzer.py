# Task-07 : Text Analyzer

#input
sentence = input("Enter a sentence : ")

#process and output
print("Original text : ",sentence)
print("Uppercase : ",sentence.upper())
print("Lowercase : ",sentence.lower())
print("Number of characters : ",len(sentence))
individual_words = sentence.split()
print("Number of words : ",len(individual_words))
count = 0
word = sentence.lower()
for character in word :
    if character in "aeiou":
        count += 1
print("Number of vowels : ",count)
count = 0
for space in sentence:
    if space == ' ':
        count += 1
print("Number of spaces : ",count)
print("Reversed text : ",sentence[::-1])