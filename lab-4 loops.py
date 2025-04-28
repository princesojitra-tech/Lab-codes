
#1
for i in range(26):
        print(chr(97 + i), end=' ')
print()

for i in range(26):
    print(chr(65 + i), sep=" ")
print()
    

#2
n=5
for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

#3
n = int(input("Enter value for n :"))
if n<=1:
    print('not a prime')

for i in range(2,10):
    if n%i==0:
        print("Number is prime")

#4
def d4(n):  
    if n < 2:
        return False 
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False 
    return True 

a = int(input("Enter any number: "))  
print("Given number is Prime:", d4(a)) 

def d42(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
            
    return sum==n
a=int(input("enter a number :"))

if d42(a):
    print(a,"is a perfect number")
else:
    print(a,"is a not perfect number")

def d43(n):
    num=str(n)
    num_digits=len(num)
    sum_of_power=0

    for digit in num:
        sum_of_power+=int(digit)**num_digits

    return sum_of_power == n

a=int(input("enter any number :"))

if d43(a):
    print(a,"is an armstrong number")
else:
    print(a,"is not an armstrong number")

def d44(n):
    return str(n)==str(n)[::-1]

a=int(input("enter any number:"))

if d44(a):
    print(a,"is pelindrome")
else:
    print(a,"is not pelindrome")


def d45(n):
    square = n**2
    return str(square).endswith(str(n))

num=int(input("enter any number:"))

if d45(num):
    print(num,"is an automorphic number")
else:
    print(num,"is not an automorphic number")

#5
limit=int(input("enter:"))
triplets = []
for a in range(1, limit + 1):
    for b in range(a, limit + 1):
        c = (a**2 + b**2) ** 0.5
        if c.is_integer() and c <= limit:
            triplets.append((a, b, int(c)))
print=(triplets)

#6
for hour in range(24):
        if hour == 0:
            print("12 Midnight")
        elif hour == 12:
            print("12 Noon")
        elif hour < 12:
            print(f"{hour} AM")
        else:
            print(f"{hour - 12} PM")

#7

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))
n_fact = 1
for i in range(1, n + 1):
 n_fact *= i
r_fact = 1
for i in range(1, r + 1):
 r_fact *= i
n_r_fact = 1
for i in range(1, n - r + 1):
 n_r_fact *= i
nCr = n_fact // (r_fact * n_r_fact)
nPr = n_fact // n_r_fact
print("The nCr is",nCr)
print("The nPr is",nPr)

#8
def d8():
    num=int(input("enter any number :"))
    fact=1
    for i in range(1,num+1):
        fact*=i
    print("factorial of",num,"is",fact)
d8()     

#9
def d9():
    n=int(input("Enter the Number:"))
    for i in range(n,0,-1):
          print(i)
d9()        

#10
def d10():
 N = int(input("Enter the number: "))  
 a, b = 0, 1  
 print("Fibonacci series:")  
 for i in range(N):  
    print(a, end=" ")  
    a, b = b, a + b  
d10()

#11
def d11():
    import math
    x = float(input("Enter x in radians: "))
    sin_x = math.sin(x)
    print(f"sin({x}) = {sin_x}")
d11()
