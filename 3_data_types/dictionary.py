

foods = {
    "malta": "🍊",
    "kela": "🍌",
    "🍇": "angoor",
    "stab": "🍓",
    "marchaky": "🌶",
    "pizza": "🍕"
}

item = foods["marchaky"] #?
item = foods["stab"] #?
item = foods["🍇"] #?
item = foods["kela"] #?

item = foods.get("kela") #?
item = foods.get("indwana") #?
item = foods.get("indwana", "🍽") #?
item = foods.get("stab", "Not found") #?
# item = foods["indwana"] #?
 
 # ===============================================================

emojis = {
   "foods": {
    "malta": "🍊",
    "kela": "🍌",
    "🍇": "angoor",
    "stab": "🍓",
    "marchaky": "🌶",
    "pizza": "🍕",
   },
   "sports":{
       "criket": "🏏",
       "football": "⚽️",
       "Tennis": "🎾",
   }
}


kela = emojis["foods"]["kela"] #?
foods = emojis["foods"] #?
k = foods["kela"] #?
k = foods["stab"] #?
# =================================================================================

foods = {
    1: "🍊",
    2: "🍌",
    3: "🍇",
    4: "🍓",
    5: "🌶",
    6: "🍕"
}

test = "🍌" in foods #?
test = 2 in foods #?
test = 3 in foods #?
test = 35 in foods #?

foods[4] = "🍟"
foods
x = foods.items() #?

it = foods.values() #?
it = foods.keys() #?
it = foods.pop(3) #?
# it = foods.pop(3) #?
it = foods.pop(3, "Not found") #?

it = foods.popitem() #?
it = foods.popitem() #?
it = foods.popitem() #?

# foods.clear()
# del foods

foods

# for i in range(1,  len(foods)):
#     print(i, foods[i])



sorted = sorted(foods) #?
