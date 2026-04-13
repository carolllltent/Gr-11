count = 0 
countdigit = 0
countspace = 0
word = input("What is your word: ").lower()

for letter in word: 
    if letter not in "aeiou": 
        count += 1

print("constanents: ", count)

for letter in word: 
    if letter in word: 
        countdigit += 1

print("digits: ", countdigit)

sentence = input("What is your sentence: ").lower()
for space in sentence: 
    if space in " ": 
        countspace += 1

print("space: ", countspace)

