#sprint 1 
for i in range(3):
    print(i)

#the output is 0, 1, 2 - the for loop stops before reaching three - it includes all numbers inside the range of 3

#sprint 2 
for i in range(2, 7, 2):
    print(i)

#the output is 2, 4, 6 - the program starts at the number two, stops at 7 and goes by 2 when counting - the range is from 2 - 7

#sprint 3
word = "DOG"
for letter in word:
    print(letter)

#The for loop runs 3 times, printing each letter of the word "DOG"

number = 1
while number < 4: 
    print (number)
    number += 1

#sprint 5 
x = 0

while x < 5:
    print(x)
    x += 1 

#what was wrong was that there was no count - meaning it would have repeated 0 over and over again 

#sprint 6 
for letter in "apple":
    if letter in "pl":
        print(letter)

#the output is ppl - includes all letters of pl 

#sprint 7
for letter in "banana":
    if letter in "an":
        print(letter)

#it prints like i expected it to because it includes all letter of an 

#sprint 8 
#x = 5
#while x > 0:
#    print(x)
#    x -= 1

for x in range (5, 0, -1): 
    print (x)



