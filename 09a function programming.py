#1.	Define three functions fun(), disp() and msg(). Store them in a list and call them one by one in a loop.
def fun():
    print("This is fun()")

def disp():
    print("This is disp()")

def msg():
    print("This is msg()")

functions = [fun, disp, msg]

for func in functions:
    func()

#2.	Suppose there are two lists, one containing numbers from 1 to 6, and other containing numbers from 6 to 1. Write a program to obtain a list that contains elements obtained by adding corresponding elements of the two lists. (hint: use map and lambda functions)
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]
result = list(map(lambda x, y: x + y, list1, list2))
print(result)

#3.	Generate the list of 10 different random numbers between -15 and 15. Create a new list by obtaining square of all numbers in a list.
import random
numbers = [random.randint(-15, 15) for i in range(10)]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(numbers)
print(squared_numbers)

#4.	Consider the following list:
lst = ['madam','Python',"malayalam",12321]
#Write a program to print those strings which are palindromes.
palindromes = list(filter(lambda x: (isinstance(x, str) or isinstance(x, int)) and str(x) == str(x)[::-1], lst))
print(palindromes)

#5.	A list contains names of Faculty Members. Write a program to filter out those names whose length is more than 8 characters.
faculty = ['John Doe', 'Jane Smith', 'Alice', 'Bob', 'Charlie Brown']
long_names = list(filter(lambda x: len(x) > 8, faculty))
print(long_names)
