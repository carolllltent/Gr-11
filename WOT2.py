total = 0

for i in range(3):
    print(i)

age = int(input("Enter age: "))

#next question 
if age > 15:
   print("You may enter")
else:
   print("You may not enter")

num = int(input("Enter number: "))


if num == "10":
   print("Ten")
else:
   print(num)

#next question 
age = int(input("What is your age "))


if age >= 12:
   print("You are not a child")
else:
   print("You are a child")

#question 1:
number = int(input("Give me a number "))


if number % 2 == 0:
   print("This number is even")
else:
   print("This number is odd")


#question 2:
number1 = int(input("Give me a number "))


if number <= 0:
   print(number * -1)
else:
   print(number)


#question 3


month = (input("Enter the month: "))


if month is ["September", "April", "November", "June", "september", "april", "november", "june"]:
   print("30 days")
elif month is ["Februrary", "februrary"]:
   print("28 days")
else:
   print("31 days")


#question 4


side1 = int(input("What is the length of side 1 "))
side2 = int(input("What is the length of side 2 "))
side3 = int(input("What is the length of side 3 "))


if side1 == side2:
   print("Isosceles")
elif side1 == side3:
   print("Isosceles")
elif side2 == side3:
   print("Isosceles")
elif side1 == side2 == side3:
   print("Equilateral")
elif side1**2 + side2**2 == side3**2:
   print("Right")
else:
   print("Scalene")


#question 5
import math
grams = int(input("What is the weight of a letter "))


if grams <=30:
   print("$0.48")
elif grams <= 50:
   print("$0.70")
elif grams <= 100:
   print("$0.90")
else:
   extra_grams = grams - 100
   factor = (extra_grams / 50)
   rounded = math.ceil(factor)
   cost = 0.90 + (rounded * 0.18)
   rounded_cost = round(cost, 2)
   print(rounded_cost)


#question 6
card = int(input("Input your card number "))


if card <= 13:
   suit = "Hearts"
elif card <= 26:
   suit = "Diamonds"
elif card <= 39:
   suit = "Spades"
else:
   suit = "Clubs"


if card in ["1", "14", "27", "40"]:
   value = "Ace"
elif card in ["11", "24", "37", "50"]:
   value = "Jack"
elif card in ["12", "25", "38", "51"]:
   value = "Queens"
elif card in ["13", "26", "39", "52"]:
   value = "King"
else:
   value = str(card)
   print(value + " of " + suit)


#question 7
a = int(input("Enter 'a': "))
b = int(input("Enter 'a': "))
c = int(input("Enter 'c': "))




if b ** 2 - 4 * a * c > 0:
   print("Two real roots!")
if b ** 2 - 4 * a * c == 0:
   print("One real root!")
if b ** 2 - 4 * a * c < 0:
   print("No real roots!")


#question 8
digit = int(input("Enter a single digit: "))




if digit == 0:
   print("zero")
elif digit == 1:
   print("one")
elif digit == 2:
   print("two")
elif digit == 3:
   print("three")
elif digit == 4:
   print("four")
elif digit == 5:
   print("five")
elif digit == 6:
   print("six")
elif digit == 7:
   print("seven")
elif digit == 8:
   print("eight")
else:
   print("nine")


#question 9
month = input("Enter your birth month (Make sure to capitalize): ")
day = int(input("Enter your birth day: "))




if month == "January":
   if day <= 19:
       print("Capricorn")
   else:
       print("Aquarius")
elif month == "February":
   if day <= 18:
       print("Aquarius")
   else:
       print("Pisces")
elif month == "March":
   if day <= 20:
       print("Pisces")
   else:
       print("Aries")
elif month == "April":
   if day <= 19:
       print("Aries")
   else:
       print("Taurus")
elif month == "May":
   if day <= 20:
       print("Taurus")
   else:
       print("Gemini")
elif month == "June":
   if day <= 20:
       print("Gemini")
   else:
       print("Cancer")
elif month == "July":
   if day <= 22:
       print("Cancer")
   else:
       print("Leo")
elif month == "August":
   if day <= 22:
       print("Leo")
   else:
       print("Virgo")
elif month == "September":
   if day <= 22:
       print("Virgo")
   else:
       print("Libra")
elif month == "October":
   if day <= 22:
       print("Libra")
   else:
       print("Scorpio")
elif "November":
   if day <= 21:
       print("Scorpio")
   else:
       print("Sagittarius")
else:
   if day <= 21:
       print("Sagittarius")
   else:
       print("Capricorn")




