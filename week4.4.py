#sprint 1
def triple(num): 
    return(num * 3)

result = triple(5)
print(result)

#sprint 2
def square(num):
    return(num * num)

result = square(5)
print(result)
    
#sprint 3
age = int(input("What is your age "))
def classify_age(age): 
    if age < 13: 
        return "Child"
    if age < 18:
        return "Teen"
    else: 
        return "Adult"

result = classify_age(age)
print(result)


