#1
import random

odd_numbers = random.sample(range(1, 100, 2), 5)
print("Original list of 5 odd integers:", odd_numbers)

even_numbers = random.sample(range(2, 100, 2), 4)
print("List of 4 even integers:", even_numbers)

odd_numbers[2] = even_numbers
print("After replacing third element with even integers:", odd_numbers)

flattened_list = []
for item in odd_numbers:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)
print("Flattened list:", flattened_list)

flattened_list.sort()
print("Sorted list:", flattened_list)

#2
import random

odd_numbers = random.sample(range(1, 100, 2), 5)
print("Original list of 5 odd integers:", odd_numbers)

even_numbers = random.sample(range(2, 100, 2), 4)
print("List of 4 even integers:", even_numbers)

odd_numbers[2] = even_numbers
print("After replacing third element with even integers:", odd_numbers)

flattened_list = []
for item in odd_numbers:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)
print("Flattened list:", flattened_list)

flattened_list.sort()
print("Sorted list:", flattened_list)

random_numbers = [random.randint(1, 50) for _ in range(20)]
print("List of 20 random integers:", random_numbers)

user_number = int(input("Enter a number to find its positions: "))
positions = [index for index, value in enumerate(random_numbers) if value == user_number]

if positions:
    print(f"The number {user_number} occurs at positions:", positions)
else:
    print(f"The number {user_number} does not occur in the list.")

#3
import random

odd_numbers = random.sample(range(1, 100, 2), 5)
print("Original list of 5 odd integers:", odd_numbers)

even_numbers = random.sample(range(2, 100, 2), 4)
print("List of 4 even integers:", even_numbers)

odd_numbers[2] = even_numbers
print("After replacing third element with even integers:", odd_numbers)

flattened_list = []
for item in odd_numbers:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)
print("Flattened list:", flattened_list)

flattened_list.sort()
print("Sorted list:", flattened_list)

random_numbers = [random.randint(1, 50) for _ in range(20)]
print("List of 20 random integers:", random_numbers)

user_number = int(input("Enter a number to find its positions: "))
positions = [index for index, value in enumerate(random_numbers) if value == user_number]

if positions:
    print(f"The number {user_number} occurs at positions:", positions)
else:
    print(f"The number {user_number} does not occur in the list.")

random_numbers_50 = [random.randint(1, 30) for _ in range(50)]
print("List of 50 random integers:", random_numbers_50)

unique_numbers = list(set(random_numbers_50))
print("List after removing duplicates:", unique_numbers)

#4
import random

odd = random.sample(range(1, 100, 2), 5)
even = random.sample(range(2, 100, 2), 4)
odd[2] = even
flat = [x for i in odd for x in (i if isinstance(i, list) else [i])]
print("Sorted List:", sorted(flat))


nums = [random.randint(1, 50) for _ in range(20)]
n = int(input("Enter number: "))
pos = [i for i, x in enumerate(nums) if x == n]
print("Positions:", pos if pos else "Not found")


nums_50 = list(set(random.randint(1, 30) for _ in range(50)))
print("Unique numbers:", nums_50)


nums_30 = [random.randint(-50, 50) for _ in range(30)]
pos_nums = [x for x in nums_30 if x > 0]
neg_nums = [x for x in nums_30 if x < 0]
print("Positive:", pos_nums)
print("Negative:", neg_nums)

#5
strings = list(["apple", "banana", "cherry", "date", "elderberry"])
for i in range(len(strings)):
    strings[i] = strings[i].upper()
print("Uppercase strings:", strings)

#6
fahrenheit = list([32, 68, 77, 104, 212])
celsius = []

for temp in fahrenheit:
    c = (temp - 32) * 5/9
    celsius.append(c)

print("Temperatures in Celsius:", celsius)

#7
stack = []

while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = input("Enter element to push: ")
        stack.append(element)
        print("Element pushed!")

    elif choice == 2:
        if not stack:
            print("Stack is empty!")
        else:
            print("Popped element:", stack.pop())

    elif choice == 3:
        if not stack:
            print("Stack is empty!")
        else:
            print("Stack elements:", stack)

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")

#8
queue = []

while True:
    print("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = input("Enter element to enqueue: ")
        queue.append(element)
        print("Element added!")

    elif choice == 2:
        if not queue:
            print("Queue is empty!")
        else:
            print("Removed element:", queue.pop(0))

    elif choice == 3:
        if not queue:
            print("Queue is empty!")
        else:
            print("Queue elements:", queue)

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")

#9
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

list3 = [num for num in list1 if num not in list2]
print("Numbers only in the first list:", list3)
