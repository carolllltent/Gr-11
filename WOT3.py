#question 6 - even numbers 
for i in range(2,20,2): 
    print(i)

#question 7 - string filter
word = input("What is your word: ")
for letter in word: 
    if letter in "ae": 
        print(letter)

#question 8 - countdown
x = 10 
while x > 0: 
    print(x)
    x -= 1

#question 9 - accumalator 
total_sum = 0
numberlist = [1, 2, 3, 4, 5]
for numbers in numberlist:
    total_sum += numbers
    print(total_sum)

#question 10 - loop + condition 
y = int(input("What is your number: "))

for x in range(1, y, 2): 
    print(x)

#More practice 
#1st question: 
for num in range(1,101): 
    print(num)

#2nd question: 
for num in range(20,41,2): 
    print(num)

#3rd question 
for num in range(31,20,-2): 
    print(num)

#4th question
num1 = int(input("What is your first number: "))
num2 = int(input("What is your second number: "))

if num1 < num2: 
    for num in range(num1, num2):
        print(num)
else: 
    for num in range(num1, num2, - 1):
        print(num)

#5th question 

import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), (500, 500), 30)
    pygame.display.flip()
    pygame.quit()

#1st question - while 
x = 0
while x <= 100: 
    print(x)
    x += 1

#2nd question - while 
colour = input("Enter your favourite colour: (type done to stop!): ")
while colour != "done": 
    colour = input("Enter your favourite colour: (Type done to stop!) ")

#3 question - while 
total = 0
count = 0
age = int(input("What is the age of the family member: (Type -1 to stop) "))

while age != -1: 
    total += age
    count += 1
    age = int(input("What is the age of the family member: (Type -1 to stop) "))

average = total//count
print(average)

#4 question - while 
number = int(input("What is your number: "))
count = 0 

while number % 2 == 0 and number != 0:
    number = number//2 
    count += 1

print(count)
    
