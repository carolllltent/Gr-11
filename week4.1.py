#sprint 1
temperature = 31

if temperature > 0: 
    print("Above freezing")
    if temperature > 30: 
        print("Freezing day")

#sprint 2 
age = int(input("What is your age: "))

if age >= 13: 
    print("Teen or older")
    if age >= 18: 
        print("adult")
else: 
    print("child")    

#sprint 3 

age = int(input("What is your age: "))
has_id = input("Do you have id? (Yes or no) ")

if age >= 13: 
    print("Teen or older")
    if age >= 18 and has_id == "yes":
        print("adult")
else: 
    print("child")    

#sprint 5 

for i in range(2):
    for j in range(3):
        print("X")

#6 X's will print because the outer condition will be multiplied by the inner condition. The outer condition controls access to the inner condition so when the outer condition is true, the inner condition will run. 
#The inner condition has to be completed first before it can move onto the next iteration of the outer condition, so the 3 iterations of the inner condition must run first before it can move onto the second iteration of the outer conditino. 

#sprint 6 
for i in range(3): 
    for j in range(1):
        print("***")

#sprint 7 
for d in range(1, 5): 
    if d % 2 == 0: 
        print(d,d,d)

