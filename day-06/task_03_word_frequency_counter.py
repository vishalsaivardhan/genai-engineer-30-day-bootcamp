# Task-03 : Word Frequency

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

for word, count in frequency.items():
    print(word, ":", count)