# ========== named functions ===========
def add(x, y): 
    return x + y

add(10, 5) #?


# ============= lambda function ==============
sum = lambda x, y: x + y

sum(12, 13) #?

# ================ local and global variables =============
global_variable = 23

def test_display():
    local_first = 45
    print(global_variable)
    print(local_first) 

test_display()

def test_display2():
    local_sec = 45
    print(global_variable)
    print(local_sec)

test_display2()
print(global_variable)


# =================== Global Keyword ==============
country = "Pakistan"

def change_country():
    global country
    country = "Iran"

    print(country)


change_country()

print(country)


# ================ nested functions ==============
def foo():
    x = 20

    def bar():
        global x
        x = 25
    
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main: ", x)

# =================== the end =============