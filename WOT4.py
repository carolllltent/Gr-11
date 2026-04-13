#question 3
num = int(input("What is your number: "))
def double(num): 
    return(num * 2)

result = double(num)
print(result)

#question 4 
score = int(input("What is your score: "))
def grade_letter(score): 
    if score >= 90: 
        return("A")
    elif score >= 80: 
        return("B")
    elif score >= 70: 
        return("C")
    else: 
        return("Below C")

result = grade_letter(score)
print(result)

#question 1 - extra practice part a 
for i in range(34, 57): 
    if 36 < i < 44: 
        i += 0 
    elif 46 < i < 54: 
        i += 0 
    else: 
        print(i, end=" ")
    
#question 1 - extra practice part b 
x = 0
for i in range(15, 39): 
    if 18 < i < 25: 
        i += 0
    elif 28 < i < 35: 
        i += 0 
    else: 
        print(i, end=" ")
        x += 1
        if x % 4 == 0: 
            print()


#question 2 - extra practice 
for i in range(4): 
    for j in range(6): 
        print("*", end='')
    print()

#question 3 - extra practice
for i in range(10): 
    for j in range(12): 
        print("*", end='')
    print()

#question 4 - extra practice 
rows = int(input("What is the number of rows: "))
columns = int(input("What is the number of columns: "))
for i in range(rows): 
    for j in range(columns): 
        print("*", end='')
    print()
#question 5 - extra practice part a
rows = 10 
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end='')
    print()

#question 5 - extra practice part b
rows = 10 
columns = 10
for rows in range(rows): 
    for columns in range(columns): 
        print("*", end='')
    print()

#question 5 - extra practice part c 
rows = 10 
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#question 5 - extra practice part d 
rows = 9 
for i in range(rows, 0, - 1):
    for j in range(i, 0, - 1):
        print(j, end="")
    print()

#question 5 - extra practice part e 
rows = 9 
for i in range(1, rows): 
    for j in range(i): 
        print("*", end="")
    print()
for i in range(rows, 0, - 1):
    for j in range(i):
        print("*", end="")
    print()

#question 6 - extra practice 
rows = 8
for i in range(1, rows):
    for j in range(rows - i): 
        print(" ", end="")
    for k in range(i, 2 * i): 
        print(k % 10, end="")
    for k in range(2 * i - 2, i - 1, -1): 
        print(k, end="")
    print()
