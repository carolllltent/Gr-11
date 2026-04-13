#sprint 1 
temperature = 32
if temperature > 0:
    if temperature > 30:
        print("Hot")
    else:
        print("Warm")
else:
    print("Cold")

#The program will print the word Hot because the temperature is above 30. The variable temperature is stored as the value of 32. The if else functions for decision making, if a condition is met, it will execute a specific block of code. 
#The first if else statement or the outer condition is checked to see if the variable is above 0 degrees in which the condition is true. Due to the outer condition being marked as true, the inner condition will run and check if the variable meets the condition. 
#Due to the condition being true for the inner condition as well, it will print "Hot" If it was not true, the else statement will act as a default alternative if it does not meet the inner condition but applies to the first outer condition. If it does not meet any of the condition, the outer else statement will act as the default condition and print cold. 

#sprint 2 

score = int(input("What is your score: "))
if score >= 50: 
    print("Pass")
    if score >= 90: 
        print("Excellent!")
    else: 
        print("Good effort")
else: 
    print("Needs improvement ")

#sprint 3 

age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
elif age >= 13:
        print("Teen")
else:
    print("Child")
