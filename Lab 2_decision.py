#Question:1
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if(a>b):
    print("First Number is Maximum")
    print("Second Number is Minimum")
else:
    print("Second Number is Maximum")
    print("First Number is Minimum")


#Question:2
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if(a>b) and (a>c):
    print( f"{a}is Greatest")
    if(b>c):
        print(f"{c} is Smallest")
    else:
        print(f"{b} is Smallest")
if(b>a) and (b>c):
    print(f"{b} is Greatest")
    if(a>c):
        print(f"{c} is Smallest")
    else:
        print(f"{a} is Smallest")
if(c>a) and (c>b):
    print(f"{c} is Greatest")
    if(b>a):
        print(f"{a} is Smallest")
    else:
        print(f"{b} is Smallest")


#Question 3
a = int(input("Enter the number: "))
if(a%2 == 0):
    print("Number is even")
else:
    print("Number is odd")


#Question 4
a = int(input("Enter the number: "))
if(a%10 == 0):
    print("Number is divisible by 10")
else:
    print("Number is not divisible by 10")


#Question 5
a = int(input("Enter your age: "))
if(a>18):
    print("Major")
else:
    print("Minor")


#Question 6
a = int(input("Enter any number: "))
print("The Length of the string is :",len(str(a)))


#Question 7
a = int(input("Enter the year: "))
if(a%4 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")


#Question 8
a = int(input("Enter the first side of triangle: "))
b = int(input("Enter the second side of triangle: "))
c = int(input("Enter the third side of triangle: "))

sum = a+b+c
if(sum%180 == 0):
    print("Perfect triangle")
else:
    print("Not a triangle")


#Question 9
a = int(input("Enter any number: "))
if(a<0):
    print(f"The absolute value of number is:{-1*a}")
else:
    print(f"The absolute value of number is:{a}")

#Question 10
l = int(input("Enter the length of the rectangle: "))
b = int(input("enter the value of breadth of the rectangle: "))
area = l * b
peri = 2 * ( l + b )
if(area > peri):
    print("Area is greater then perimeter")
else:
    print("Perimeter is greater then area")

#Question 11
x1 = int(input("Enter the value of x1: "))
y1 = int(input("Enter the value of y1: "))
x2 = int(input("Enter the value of x2: "))
y2 = int(input("Enter the value of y2: "))
x3 = int(input("Enter the value of x3: "))
y3 = int(input("Enter the value of y3: "))
m1 = (y2 - y1)/(x2 - x1)
m2 = (y3 - y2)/(x3 - x2)
if(m1 == m2):
    print("All three point lies on same line")
else:
    print("These points do not lies on same line")

#Question 12
import math
r = 5
print(f"The radiuas of the circle is: {r}")
x = 0
y = 0
print(f"The Center of the circle is {(x ,y)}")
a = int(input("Enter the x coordinate of the point: "))
b = int(input("Enter the y coordinate of the point: "))
d = math.sqrt((pow((x - a),2) + pow((y - b),2)))
if(d == r):
    print("The point lies on the circle")
elif(d < r):
    print("the point lies inside the circle")
else:
    print("The point lies outside the circle")

#Question 13
a = int(input("Enter number between 1 to 19: "))
if(a == 0):
    print("Zero")
elif(a == 1):
    print("One")
elif(a == 2):
    print("two")
elif(a == 3):
    print("three")
elif(a == 4):
    print("four")
elif(a == 5):
    print("five")
elif(a == 6):
    print("six")
elif(a == 7):
    print("seven")
elif(a == 8):
    print("eight")
elif(a == 9):
    print("nine")
elif(a == 10):
    print("ten")
elif(a == 11):
    print("eleven")
elif(a == 12):
    print("twelev")
elif(a == 13):
    print("thirteen")
elif(a == 14):
    print("forteen")
elif(a == 15):
    print("Fifteen")
elif(a == 16):
    print("sixteen")
elif(a == 17):
    print("seventeen")
elif(a == 18):
    print("eighteen")
else:
    print("Ninteen")

#Question 14
a = int(input("Enter the marks of maths: "))
b = int(input("Enter the marks of science: "))
c = int(input("Enter the marks of hindi: "))
avg = (a + b + c) / 3
print(f"The average of all marks is:{avg}")
if( a < 39 ):
    print("FAIL in maths")
elif(a >= 0 and a <= 39):
    print("F grade in maths")
elif(a >= 40 and a <= 44):
    print("P grade in maths")
elif(a >= 45 and a <= 49):
    print("C grade in maths")
elif(a >= 50 and a <= 54):
    print("B grade in maths")
elif(a >= 55 and a <= 59):
    print("B+ grade in maths")
elif(a >= 60 and a <= 69):
    print("A grade in maths")
elif(a >= 70 and a <= 79):
    print("A+ grade in maths")
elif(a >= 80 and a <= 100):
    print("O grade in maths")
else:
    print("Enter valid marks in Maths")
if( b <39):
    print("FAIL in Science")
elif(b >= 0 and b <= 39):
    print("F grade in science")
elif(b >= 40 and b <= 44):
    print("P grade in science")
elif(b >= 45 and b <= 49):
    print("C grade in science")
elif(b >= 50 and b <= 54):
    print("B grade in science")
elif(b >= 55 and b <= 59):
    print("B+ grade in science")
elif(b >= 60 and b <= 69):
    print("A grade in science")
elif(b >= 70 and b <= 79):
    print("A+ grade in science")
elif(b >= 80 and b <= 100):
    print("O grade in science")
else:
    print("Enter valid marks in science")
if( c < 39):
    print("FAIL in Hindi")
elif(c >= 0 and c <= 39):
    print("F grade in hindi")
elif(c >= 40 and c <= 44):
    print("P grade in hindi")
elif(c >= 45 and c <= 49):
    print("C grade in hindi")
elif(c >= 50 and c <= 54):
    print("B grade in hindi")
elif(c >= 55 and c <= 59):
    print("B+ grade in hindi")
elif(c >= 60 and c <= 69):
    print("A grade in hindi")
elif(c >= 70 and c <= 79):
    print("A+ grade in hindi")
elif(c >= 80 and c <= 100):
    print("O grade in hindi")
else:
    print("Enter valid marks in hindi")






    



    


    
        
