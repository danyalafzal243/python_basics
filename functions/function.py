# ============== example 1 ====================
def greet_user():
    print("Welcome !!")


greet_user() # calling function


# ==================== function parameters example 1 ================
def add(val1, val2):
    print(val1 + val2)

add(4, 6)

# ==================== function parameters example 2 ================
def sub(val1, val2):
    res = val1 - val2 #?

response = sub(40, 6) #?

# =================== function return result ====================

def add_return_value(v, u):
    res  = v + u #?
    return res


result = add_return_value(3, 6) #?


# ============  random function example ================
import random

def chay_ba_sok_rawri():
    group = ["Danyal", "Mohsin", "Zohaib", "Ihtisham", "Bilal"]
    kas = random.choice(group)
    return kas

print(chay_ba_sok_rawri()) 

