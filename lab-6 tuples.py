#1
names_list = [('Jay', 'Jenil'), 'Kiya', ('Prashil', 'Bhavya'), 'Aesha', ('Prince', 'Aayush')]

boys_count = 0
girls_count = 0

for name in names_list:
    if isinstance(name, tuple):
        boys_count += 1
    else:
        girls_count += 1

print("Number of boys:", boys_count)
print("Number of girls:", girls_count)

print(" ")

#2

students = [(1, 'Prashil', 20), (2, 'Aayush', 19), (3, 'Bhavya', 21), (4, 'Jenil', 18)]

roll_numbers = []
names = []
ages = []

for student in students:
    roll_no, name, age = student
    roll_numbers.append(roll_no)
    names.append(name)
    ages.append(age)

print("Roll Numbers:", roll_numbers)
print("Names:", names)
print("Ages:", ages)

print(" ")

'''
#3
from datetime import date

date1 = (21, 2, 2025)
date2 = (1, 3, 2025)

d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])

days_difference = (d2 - d1).days

print("Number of days between the two dates:", days_difference)

#4
food_items = [('Apple', 3), ('Banana', 1), ('Pizza', 12), ('Burger', 8), ('Ice Cream', 5)]

sorted_food_items = sorted(food_items, key=lambda item: item[1], reverse=True)

print("Food items sorted by price in descending order:")
for item in sorted_food_items:
    print(item)

#5

list = [(1,9), (), (3, 4), (5, 6), (), (7, 8)]

filtered_list= [t for t in list if t]

print("List after removing empty tuples", filtered_list)

#6
my_tuple = (1, 2, 3, 4)

my_list = list(my_tuple)

my_list[1] = 99

my_tuple = tuple(my_list)

print(my_tuple)

#6
my_tuple = (1, 2, 3, 4)

my_list = list(my_tuple)

del my_list[1]

my_tuple = tuple(my_list)

print(my_tuple)

'''