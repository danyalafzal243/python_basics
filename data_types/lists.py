scores = [12, 33, 44, 33, 50, 60]
scores[-1] #?
scores[-6] #?
scores[-6:-1] #?

#  slice
scores[1:3] #?
scores[3:] #?


scores[3] = 500

print(scores)
# ====================================
s = [11, 22, 33, 44]
print(s)

s.append(40)
s.append(60)
print(s)
# ==============
a = [11, 33]
b = [111, 333]
b = a + b #?
# ========================
marks = [11, 22, 30]
print(marks)

marks.remove(22)
print(marks)
# =========================
x = [11, 22, 30]
print(x)
x.pop() #?
print(x)

x.clear()
print(x)
# =========================
y = [11, 22, 30]
print(y)
del y[1]

print(y)

del y
# print(y)








