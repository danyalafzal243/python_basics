# ================== arguments example ================
def greet(name, msg):
    print("Hello ", name + ', ' + msg)
    print(f"Hello {name}, {msg}")

greet("Monica", "Good morning!")

# ================== default arguments example ================
def add(v, u = 10):
    res = v + u #?
    return res

add(5, 7) #?
add(5) #?

# ================== default arguments example ================
def sub(v, u = 10):
    res = v - u #?
    return res

sub(v = 20, u = 7) #?
sub(50) #?

# ================= Arbitrary Arguments ============
def greet(*args):
    for name in args:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "John")

# ======================= Recursion ============
    
# --- while loop -----
def print_pakistan_using_while_loop():
    i = 1
    while(i < 10):
        print(f"{i}, pakistan using while loop")
        i += 1

print_pakistan_using_while_loop()

# ----- using recursion ----------
def print_pakistan_using_while_recursion(number_of_times):
    print(f"{number_of_times}, pakistan using recursion")

    if(number_of_times < 1):
        return
    
    number_of_times -= 1
    print_pakistan_using_while_recursion(number_of_times)

print_pakistan_using_while_recursion(10)

# task -> Working of a recursive factorial function

