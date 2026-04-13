#sprint 1 
num = int(input(" What is your number: "))

def cube(num): 
    return(num * num * num)
result = cube(num)
print(result)
def is_even(num): 
    if num % 2 == 0: 
        return("even")
    else: 
        return("odd")

result2 = is_even(num)
print(result2)

#review

def calculate_tax(price):
    return(1.13*price)
    
total=100
result=calculate_tax(total)

print("The total is: ", result)


