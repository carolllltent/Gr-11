#Level 2 
#Write a function that defines a rectangle. The function takes the x and y coordinates of point A,
#width and height. Use this information to display the coordinates of all four vertices (corners) of
#the rectangle in the order ABCD. Note that x, y, width and height are always values greater than 0.
#Prompt the user to input x, y, width and height on separate lines.
#Again, NO GRAPHICS REQUIRED!!! AD and BC are width, AB and DC are height.
#For example:
#define rectangle (x, y, width, height)
# values passed to the function (3, 5, 17, 21)
# expected output:
# The rectangle has vertices A(3, 5), B(3, 26), C(20, 26) and D(20, 5)

x = int(input("What is the x value? "))
y = int(input("What is the y value? "))
width = int(input("What is width? "))
height = int(input("What is height? "))

def rect(x,y,width,height):
    A = (x,y)
    B = (x, y + height)
    C = (x + width, y + height)
    D = (x + width, y)
    print("The verticies for your rectangle is: ")
    print(A, B, C, D)

result = rect(x,y,width,height)

#Level 3
#Continue from level 2 to prompt the user also to input a point (called P) with separate
#prompts for the x-coordinate and the y-coordinate. Determine if that point P lies on, within or outside the rectangle.
#For example:
#define rectangle ( x, y, width, height, Px, Py)
#Please enter the x coordinate of P. 8
# Please enter the y coordinate of P. 12
# values passed to the function (3, 5, 17, 21, 8, 12)
#expected output:
# The rectangle has vertices A(3, 5), B(3, 26), C(20, 26) and D(20, 5)
# (8, 12) is on or within the rectangle.

x = int(input("What is the x value? "))
y = int(input("What is the y value? "))
width = int(input("What is width? "))
height = int(input("What is height? "))
Px = int(input("What is the x value of point P "))
Py = int(input("What is the y value of point P "))

def rect(x,y,width,height,Px,Py):
    A = (x,y)
    B = (x, y + height)
    C = (x + width, y + height)
    D = (x + width, y)
    print("The verticies for your rectangle is: ")
    print(A, B, C, D)
    P = (Px, Py)
    if x > Px < x + width and y > Py < y + height: 
        print("Point P", P, " lies within the rectangle")
    elif Px < x or Px > x + width and Py < y or Py > y + height: 
        print("Point P", P, "outside of the rectangle")
    else: 
        print("Point P", P, " lies on the rectangle")
    
result = rect(x,y,width,height,Px,Py)

#Level 3+ 
#Level 3 is modified so that the point is inputted by the user in the form: (x,y).
#For example:
#define rectangle ( x, y, width, height, Px, Py)
#Please enter the point in the form (x, y): (8,12)
#values passed to the function (3, 5, 17, 21, 8, 12)
#expected output:
#The rectangle has vertices A(3, 5), B(3, 26), C(20, 26) and D(20, 5)
#(8, 12) is on or within the rectangle.

x, y = input("Enter two single-digit numbers: ")
point = (int(x), int(y))
print(x)
width = int(input("What is width? "))
height = int(input("What is height? "))
Px,Py = input("What is the x and y value of point P ")
pointP = (int(Px), int(Py))
#attempt to input points through coordinates w/out seperate values e.g input x value input y value
def rect(x,y,width,height,Px,Py):
    A = (x,y)
    B = (x, y + height)
    C = (x + width, y + height)
    D = (x + width, y)
    print("The verticies for your rectangle is: ")
    print(A, B, C, D)
    P = (Px, Py)
    if x > Px < x + width and y > Py < y + height: 
        print("Point P", P, " lies within the rectangle")
    elif Px < x or Px > x + width and Py < y or Py > y + height: 
        print("Point P", P, "outside of the rectangle")
    else: 
        print("Point P", P, " lies on the rectangle")
    
result = rect(x,y,width,height,Px,Py)

