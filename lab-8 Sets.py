#1
words_list = ["apPle", "baNana", "cheRry", "dAte", "elderbErry"]

uppercase_set = {word.upper() for word in words_list}
print("Set of uppercase words:", uppercase_set)

lowercase_set = {word.lower() for word in words_list}
print("Set of lowercase words:", lowercase_set)


#2
'''
import random
random_num=[random.randint(15,45) for _ in range(10)]
print(random_num)

i=0
for i in num:
    i+=1
    if num[i]>35:
        del num[i]

'''
import random

random_numbers = {random.randint(15, 45) for _ in range(10)}
print("Original set:", random_numbers)

lessthan_30_count = sum(1 for num in random_numbers if num < 30)
print("Count of numbers less than 30:", lessthan_30_count)

filtered_numbers = {num for num in random_numbers if num <= 35}
print("Set after deleting numbers greater than 35:", filtered_numbers)


#3
names = set()

names.update(["Alice", "Bob", "Charlie", "Diana", "Edward"])
print("After adding names:", names)

names.remove("Charlie")
names.add("Chris")
print("After modifying a name:", names)

names.remove("Alice") 
names.discard("Bob")
print("After deleting two names:", names)


#4
names = {"Alice", "Bob", "Annie", "Brian", "Andrew", "Bella", "Amanda"}

names_starting_with_A = set()
names_starting_with_B = set()

for name in names:
    if name.startswith("A"):
        names_starting_with_A.add(name)
    elif name.startswith("B"):
        names_starting_with_B.add(name)

print("starting with A:", names_starting_with_A)
print("starting with B:", names_starting_with_B)
