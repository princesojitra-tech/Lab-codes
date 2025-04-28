#1
def count_lower_upper(str):
    count_upper = 0
    count_lower = 0
    for char in str:
        if("A" <= char <= "Z"):
            count_upper += 1
        else:
            count_lower += 1    
    return {'No. of uppercase alphabets': count_upper ,'No. of lowercase alphabets': count_lower}

str = input("Enter the string which only contains alphabets : ")
print(count_lower_upper(str))

#2

def compute(n):
    nn = int(str(n) * 2)
    nnn = int(str(n) * 3)
    nnnn = int(str(n) * 4)
    
    return n + nn + nnn + nnnn

for i in range(4, 8):
    print(f"compute({i}) = {compute(i)}")

#3
def create_array(x, y, z, value):
    return [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]

array = create_array(3, 4, 5, 7)
for layer in array:
    print(layer)

#4
def sum_avg(n):
    subjects = []
    for i in range(1, n+1):
        name = input(f"Enter the name of subject {i} : ")
        marks = input(f"Enter marks for {name} : ").strip()
        subjects.append((name, marks))

    total = sum(int(marks) for _, marks in subjects if marks.isdigit())
    average = total / len(subjects)

    print(f"\nTotal Marks : {total}")
    print(f"Average Marks : {average}")

sum_avg(5)    

#5
import string

def ispangram(s):
    alphabet_set = set(string.ascii_lowercase)
    return alphabet_set <= set(s.lower())

test_sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Crazy Fredrick bought many very exquisite opal jewels"
]

for sentence in test_sentences:
    print(f'"{sentence}" is a pangram: {ispangram(sentence)}')

str = input("\nEnter the string : ")
print(f'"{str}" is a pangram: {ispangram(str)}')

#6
def create_tuple_list(end_value):
    return [(x, x**2, x**3) for x in range(1, end_value + 1)]

end_value = int(input("Enter the End Value : "))
print(create_tuple_list(end_value))

#8
def convert(s):
    unique_sorted_words = sorted(set(s.split()))
    return ' '.join(unique_sorted_words)

test_string = "banana apple orange apple mango banana"
print(convert(test_string))

str = input("\nEnter the string : ")
print(convert(str))

#9
def count_alpha_digits(str):
    count_alpha = 0
    count_digit = 0

    for element in str:
        if(65<=ord(element)<=90 or 97<=ord(element)<=122):
            count_alpha+=1

    for element in str:
        if(48<=ord(element)<=57):
            count_digit+=1
            
    print({"No. of alphabets in the string is" : count_alpha, "No. of digits in the string is" : count_digit})

str = input("Enter the string : ")
count_alpha_digits(str)

#10
from collections import defaultdict
import string

def frequency(input_string):

    translator = str.maketrans('', '', string.punctuation)
    cleaned_string = input_string.translate(translator)
    words = cleaned_string.split()

    word_freq = defaultdict(int)
    for word in words:
        word_freq[word] += 1
    sorted_words = sorted(word_freq.keys())
    sorted_freq = {word: word_freq[word] for word in sorted_words}
    return sorted_freq

input_string = input("Enter the string : ")
result = frequency(input_string)
print(result)

#11
def create_list():
    list1 = input("Enter the elements for list1 separated by space : ").split()
    list2 = input("Enter the elements for list2 separated by space : ").split()

    return list(set(list1) & set(list2))
print("Intersection of Two Lists :-",create_list())  

#12
def prime_factors(n, divisor=2):
    if n <= 1:
        return []
    if n % divisor == 0:
        return [divisor] + prime_factors(n // divisor, divisor)
    else:
        return prime_factors(n, divisor + 1)

num = int(input("Enter a positive integer: "))
if num > 0:
    print("Prime factors:", prime_factors(num))
else:
    print("Please enter a positive integer.")

#13
def binary_equivalent(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return binary_equivalent(n // 2) + str(n % 2)

num = int(input("Enter a positive integer: "))
if num >= 0:
    print("Binary equivalent:", binary_equivalent(num))
else:
    print("Please enter a non-negative integer.")

#14
def count_vowels(s, index=0):
    vowels = "aeiouAEIOU"
    if index == len(s):
        return 0
    return (1 if s[index] in vowels else 0) + count_vowels(s, index + 1)

user_input = input("Enter a string: ")
print(f"Number of vowels in the string: {count_vowels(user_input)}")

#15
def reverse_list(lst):
    if not lst:  
        return []
    return [lst[-1]] + reverse_list(lst[:-1]) 

numbers = input("Enter the elements for list1 separated by space : ").split()
print("Original List :-",numbers)
print("Reversed List :-",reverse_list(numbers))  

#16
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))

result = power(a=a, b=b)
print(f"{a}^{b} = {result}")

#17
def sanitize_list(lst, index=0):
    if index == len(lst):
        return
    if lst[index] < 0:
        lst[index] = 0
    sanitize_list(lst, index + 1)

lst = list(map(int, input("Enter list elements separated by space: ").split()))

sanitize_list(lst)
print("Sanitized list:", lst)

#18
def average_recursive(lst, index=0, total=0):
    if index == len(lst):
        return total / len(lst) if len(lst) > 0 else 0
    return average_recursive(lst, index + 1, total + lst[index])

lst = list(map(int, input("Enter list elements separated by space: ").split()))

avg = average_recursive(lst)
print("Average of the list:", avg)

#19
def string_length_recursive(s, index=0):
    if index == len(s):
        return index
    return string_length_recursive(s, index + 1)

s = input("Enter a string : ")
print("Length of the string:", string_length_recursive(s))

#20
def fun():
    return "fun() exicuted."

def disp():
    return "disp() exicuted."
    
def msg():
    return "msg() exicuted."   

lst = [fun(), disp(), msg()]        

for l in lst:
    print(l)

#21
def add_elements_of_lists():
    lst1 = [1,2,3,4,5,6]
    lst2 = [6,5,4,3,2,1]

    lst = list(map(lambda i, j : i + j, lst1, lst2))
    print(lst)

add_elements_of_lists()    

#22
import random

def square_of_random_nums():
    lst = [random.randrange(-15,16) for _ in range(10)]
    print(f"Original List of Numbers : {lst}")
    lst = list(map(lambda x : x*x, lst))
    print(f"List of square of Numbers : {lst}")

square_of_random_nums()    

#23
def check_palindrom():
    lst = ['madam','Python','malayalam',12321]
    lst = list(filter(lambda s: str(s) == str(s)[::-1], lst))
    print(lst)

check_palindrom()    

#24
def name_char_check(lst):
    filtered_lst = list(filter(lambda s : len(s) > 8,lst))
    return filtered_lst

lst = input("Enter names of Faculty Members separated by space : ").split()
print(name_char_check(lst))









