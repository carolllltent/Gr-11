#sprint 1 
x = 15

if x > 20:
    print("A")
elif x > 10:
    print("B")
else:
    print("C")

#The variable "x" stores value as the number 15 through the direct assignment of using the equals sign (=). So, through the assignment operator, the variable "x" is assigned the interger value of 15. 
#The if-else statement enables conditional branching in which it allows the program to make specific decisions if it meets the condition or if it doesnt. In this case, x is 15 so it is greater than 10, leading to the result printing B. If x was another value or it was stored as another integer, the program would run and execute a different block of code. 

#sprint 2 

age = int(input("Enter age: "))

if age >= 20:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

#The problem with the code is that when the first condition was met, which is that if age was older or equal to 13, it would be considered as a teen regardless. This is because the computer is not allowed to inference code for us in which they decide whether or not it stops at a certain age. 
#The computer evaluates each condition as specified, from top to bottom so as long as the variable is over 13, which was the first condition met, it will not move towards other condtiions. Since the first condition was evaluated as true, that line of code was executed and all other conditions in the chain were skipped. 
#To fix this, the order of the chains needed to be switched in which, if the age was over 20, then that condition will be met and other lines will be skipped. However, as long as the variable is over 13, it cannot inference that it is over 20 so it will skip over that line, despite it being untrue. To get a more accurate result, the chains needed to be organized from oldest to youngest because you cannot decrease in age, for example, if the age is over 13, it could account for being over 20 but an age being over 20 cannot be the same as an age being over 13. 

#sprint 3

grade = int(input("Enter your percentage: "))

if grade >= 90: 
    print("You get an A+")
elif grade >= 80: 
    print("You get a A")
elif grade >= 70: 
    print("You get a B")
elif grade >= 60: 
    print("You get a C")
elif grade >= 50: 
    print("You get a D")
else: 
    print("You get an F")

#use true or false to explain 
