# ================ example 1 ================
i = 0
while(i < 6):
    i += 1
    print(i, " Code to execute")

print("rest of code") #?

# ================ example 2 ================
user_choice = 'y' 
i = 0
while(user_choice == 'y'):
    i += 1
    print(i, " YES")
    user_choice =  input("do you want to execuate ????? y = YES, n = NO  : ")


# ================= continue ==============
customers = ["ali", "khan", "jawad"]

for x in customers:
    if(x == 'ali'):
        continue
    print(x)

for x in range(30):
    if(x % 2 == 0):
        continue

    print(x)
    
# ============== break =============
for x in range(30):
    if(x == 20):
        break

    print(x)


# =====================

while(4 == 4):
    print("Happy coding!!! ")

    is_yes = input("want to execute ?? y for yes ")
    if(is_yes == 'y'):
        continue    
    else:
        break

# ========================================= 
if(True):
    pass



