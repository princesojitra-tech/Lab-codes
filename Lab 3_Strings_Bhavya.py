#Question 1 :
a = input("Enter any string: ")
print("There are ",a.count('a') + a.count("e") + a.count("i") +a.count("o") + a.count("u"), "Vowels in your String")
#method 2
s = input("Enter any string: ")
vowels = "aeiouAEIOU"
count  = sum(s.count(vowel) for vowel in vowels)
print("Numbers of vowels: ", count)

#Question 2 :
#Question 3:
b = input("Enter 1st string: ")
c = input("Enter 2nd string: ")
if(b in c):
    print("1st string is present in 2nd string")
elif(c in b):
    print("2nd  string is present in 1st string")
else:
    print("Both are Different string")

#Question 4: #wrong logic
'''d = input("Enter 1st string: ")
e = input("Enter 2nd string: ")
if(d in e):
    print("1st string is present in 2nd string")
    f = e - d
    print("After removing it the string is :", f)
elif(e in d):
    print("2nd  string is present in 1st string")
    g = (d - e)
    print("After removing it the string is :", g)
else:
    print("Both are Different string")'''
#Jordaar Logic
original = input("Enter the original string: ")
remove = input("Enter the string to remove: ")

index = original.find(remove)

if index != -1:  # If found
    original = original[:index] + original[index+len(remove): ]
print("Final string:", original)
