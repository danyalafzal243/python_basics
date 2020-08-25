# ================= Assingment operators ================
# +=
age = 12 #?

# (age += 2) == (age = age + 2)
age += 2 #?
age = age + 2 #?

# -=
marks = 45 #?
marks -= 5 #?
marks = marks - 5 #?

# *= s
transfer = 10
transfer *= 2 #?
transfer = transfer * 2 #?

# # /= 
# x = 63
# x /= 3 #? 

# print(x)

# %= 
# runs = 14  #?
# runs %= 3 # (runs = runs % 3) => 14 % 3 => 2#?
# print(runs)

# =================  Identity operators in Python =================
# is, is not

weight_1 = 45
weight_2 = 45
weight_3 = 40

# is operator
res = weight_1 is weight_2 #?
res = weight_1 is weight_3 #?
res = weight_2 is weight_3 #?


# is not operator
res = weight_1 is not weight_2 #?
res = weight_1 is not weight_3 #?
res = weight_2 is not weight_3 #?

customers = ["bilal", 'jawad', 'faisal'] #?
res = "bilal" in customers #?
res = "tariq" in customers #?

res = "bilal" not in customers #?
res = "tariq" not in customers #?

weights = [11, 22, 33, 44, 55, 66]
res = 11 in weights #?
res = 131 in weights #?
# Tuples, string, sets, dictionary, list
