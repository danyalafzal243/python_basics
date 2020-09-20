# ================ declare ==================
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} 
print(digits)

digits.pop() 
print(digits)

is_in_set =  6 in digits #?

# =============== union =================

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 8}


u = a.union(b) #?
i = a.intersection(b) #?
d = a.difference(b) #?

# ============================================


f = {1, 2, 3, 4, 5}
s = {4, 5, 6, 8}

f.update(s)

print(f)
