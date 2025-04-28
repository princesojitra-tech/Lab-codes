#1

def create_dict():
    user_dict = {}
    num_entries = int(input("How many key-value pairs do you want to enter? "))

    for i in range(num_entries):
        key = input(f"Enter key {i + 1}: ")
        value = input(f"Enter value for {key}: ")
        user_dict[key] = value

    return user_dict    

print("Create dict1:-")
dict1 = create_dict() 
print("\nCreate dict2:-")    
dict2 = create_dict()
print("\nCreate dict3:-")
dict3 = create_dict()

print("The Dictionary 01 :",dict1)
print("The Dictionary 02 :",dict2)
print("The Dictionary 03 :",dict3)

dict4 = {**dict1, **dict2, **dict3}
print("The Dictionary 04 :",dict4)

#2

def check_empty_dict(dictname,dict):

    if not dict:
        print(f"{dictname} is Empty.")
    else:
        print(f"{dictname} is not Empty.")   


dict1 = {"01":"Dhruv", "02":"Nariya"} 
check_empty_dict("dict1",dict1)
dict2 = {}
check_empty_dict("dict2",dict2)

#3

def create_employee_dict():
    employee_dict = {}
    num_employees = int(input("Enter the number of employees: "))

    for i in range(num_employees):
        dept_name = input(f"Enter department name for employee {i + 1}: ")
        emp_roll_no = input(f"Enter employee roll number for employee {i + 1}: ")
        salary = float(input(f"Enter salary for employee {i + 1}: "))

        if dept_name not in employee_dict:
            employee_dict[dept_name] = {}
        employee_dict[dept_name][emp_roll_no] = salary

    return employee_dict

def find_min_max_salary(employee_dict):
    dept_min_max = {}

    for dept_name, employees in employee_dict.items():
        salaries = list(employees.values())
        min_salary = min(salaries)
        max_salary = max(salaries)
        dept_min_max[dept_name] = {"Min Salary": min_salary, "Max Salary": max_salary}

    return dept_min_max

employee_dict = create_employee_dict()
print("\nEmployee Data:", employee_dict)

dept_min_max = find_min_max_salary(employee_dict)
print("\nDepartment-wise Minimum and Maximum Salaries:")
for dept_name, salaries in dept_min_max.items():
    print(f"Department {dept_name}: Min Salary = {salaries['Min Salary']}, Max Salary = {salaries['Max Salary']}")

#4

def char_frequency():
    input_str = input("Enter a string: ")  
    char_frq = {}

    for char in input_str:
        if char in char_frq:
            char_frq[char] += 1
        else:
            char_frq[char] = 1

    print("Character frequency:", char_frq)


char_frequency()

#5

def create_dict(key_prompt, value_prompt):
    user_dict = {}

    for i in range(num_entries):
        key = input(f"Enter {key_prompt} {i + 1}: ")
        value = int(input(f"Enter {value_prompt} of {key}: "))
        user_dict[key] = value

    return user_dict 

def count_TotalBill():
    total_bill = 0

    for item, quantity in grocery_quantities.items():
        if item in grocery_prices:
            total_bill += grocery_prices[item] * quantity
        else:
            print(f"Warning: '{item}' not found in the price dictionary.")

    return total_bill

num_entries = int(input("Enter No. of Grocery items which you want to buy : "))
print("\nDictionary of Grocery items along with their price :-")
grocery_prices = create_dict("Grocery item","Price")
print("\nDictionary of Grocery items along with their quantity :-")
grocery_quantities = create_dict("Grocery item","Quantity")

print(f"\n{grocery_prices}")
print(grocery_quantities)
print("\nTotal bill: ₹", count_TotalBill())

