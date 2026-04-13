#sprint 1

total = 0

for i in range(1, 4):
    total += i
x = 0
while x < total:
    print(x)
    x += 2

#Total is 6 because i will be 1, 2, and 3 meaning that it will the total will be the sum of i. So from the past values already inputted into memory, in the range, the total will be 1 + 2 = 3, 3 + 3 = 6. The total is the final sum of i, being 6. 
#0, 2, and 4 will print because x initially starts off as 0, the condition of being greater than the total 6 is true. Then count increases by 2, in which x = 0, the condition is still true so 2 will print. Finally, the count increases again by 2, being 4, the condition is true so it prints. However, when the count becomes 6, the condition is not true, it will not print. 
#There is a total of iterations is 3 - from the range of 1-4. 

#sprint 2

word = "school"
index = 0

while index < len(word):
    print(word[index])
    index += 1

#The index is 6 because it continously adds 1 for every iteration it goes through, it evaluates if the index is less than the lenght of the word so it will stop adding once it becomes longer than the word. It will stop at 6 
#The code stops because the while condition now becomes false, in which the index will be greater than the lenght of the word. Because of the strict condition, the program will not continue when the condition is false. 
#The difference between a for letter in word and a while loop is that a for loop is more of an automated process in which it does not evaluate every single time on whether or not the condition exceeds the lenght of the word but it will evaluate if it matches up for every letter in the word. In this case a while loop requires much more manual control. 

#sprint 3 
for letter in "apple":
    if letter in "aeiou":
        print(letter)
    else:
        print("No vowel")

#The problem is that it does not account for all vowels in which it it will only account for the two vowels a and e. This isn't what we want because we want to check for all vowels if in which the word was ocean, then it would say o is not a vowel which is untrue. 

#sprint 4
word = input("What is your word: ")
count = 0
for letters in word:
   if letters in "aeiouAEIOU":
       count += 1
print(count)





