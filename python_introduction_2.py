# =============== Python Variables, Constants and Literals =================

number = 100000
print(number)

number = 1.1
print(number)


# Example 2: Changing the value of a variable
college_name = 'Lundkhwarh'
print(college_name)

college_name = 'Mardan'
print(college_name) 

# Example 3: Assigning multiple values to multiple variables
student_name, college_name, degree = 'Ali', "Mardan", "Bs"
print(student_name, college_name, degree)


# ------------------ Literals ------------------
# Numeric
unit = 12
price = 56.67

print("Unit => ", type(unit), "price => ", type(price))

# String literals
phrase = 'Example 7: How to use string literals in Python?'
char = 'c'

print("phrase => ", type(phrase), "char => ", type(char))

# Boolean literals
is_raining = False
is_winter = True

print("is_raining => ", type(is_raining), "is_winter => ", type(is_winter))

# Literal Collections
customers = ["Ali", "Ali", "Jawad", "Faisal"] # list
facts = ('LITTER', 'BARREL') # tuple
vowels = {'a', 'e', 'i' , 'o', 'u'} #set
map = {
    'name': "Saeed khan",
    'age': 32,
    'cell': "0302020206"
} # dictionary


print(type(customers))
print(type(facts))
print(type(vowels))
print(type(map))


