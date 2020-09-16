scores = (12, 33, 44, 33, 50, 60)
scores[-1] #?
scores[-6] #?
scores[-6:-1] #?
scores[0: 3] #?

print(scores)
#  slice
scores[1:3] #?
scores[3:] #?

print(scores)

scores.count(50) #?

# ==================
for x in scores:
    print(x)

for x in enumerate(scores):
    print(x)
    print(x[0])
    print(x[1])

