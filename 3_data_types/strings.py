phrase = "python Forr all"
phrase[9] #?

x = phrase.replace("rr", 'r') #?
print(phrase)
print(x)

# ===========================
s = phrase[:9] #?
s = phrase[3:6] #?

phrase.find("all") #?
phrase.find("gul khan") #?

lower = phrase.lower() #?
upper = phrase.upper() #?
cap = phrase.capitalize() #?

arr = phrase.split(" ") #?
# =========================


for x in phrase:
    print(x)

for x in enumerate(phrase):
    print(x)

for i, x in enumerate(phrase):
    print(i)
    print(x)
