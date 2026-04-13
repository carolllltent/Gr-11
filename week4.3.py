#sprint 1
def check_age(age): 
    if age >= 18: 
        print("Adult")
    else: 
        print("Minor")

check_age(20)
        
#sprint 2

def check_temperature(temperature): 
    if temperature > 0: 
        if temperature > 30: 
            print("Hot")
        else: 
            print("Warm")
    else: 
        print("Cold")        

check_temperature(35)

#sprint 3
#def check_number():
    #number = 5
    #if number > 0:
    #print("Positive")

#check_number()

def check_number(number):
    if number > 0:
        print("Positive")

check_number(5)

#didnt call the function correctly
#no indentation after if statement 
#doesnt have a parameter - if wants to call it needs a parameter for more flexibility 

#sprint 4 
def check_temperature(temperature): 
    if temperature > 0: 
        if temperature > 30: 
            print("hot")
        else: 
            print("warm")
    else: 
        print("cold")

check_temperature(25)
check_temperature(31)

#sprint 5
def check_age(age): 
    if age > 18: 
        print("adult")
    elif age > 13: 
        print("teen")
    else: 
        print("child")

check_age(12)
check_age(18)
check_age(25)
    
#sprint 6
#What is a parameter: 
#
#What happens when we call check_age(18): 