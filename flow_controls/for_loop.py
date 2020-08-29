# ============== for loop ==============
students = ["faisal", "karim", "gul khan", "jawad"]
for x in students:
    print(x)

# ----------     simiple array example 1  -------------

marks = [3, 4, 5, 10, 12, 14, 6]
for m in marks:
    print(m)

# ---------    simiple array example 2   ---------------

for x in range(0, len(marks)):
    print(x)
    val = marks[x]
    print(val)


#----------------- 
animals = [
    {
        'type': '🐕',
        'name': 'rambo',
        'owner': 'Rabnawaz',
        'age': 12
    },
    {
        'type': '🐒',
        'owner': 'Habib',
        'name': 'shah rukh',
        'age': 15
    },
    {
        'type': '🐎',
        'owner': 'Bhadar khan',
        'name': 'Sheeno',
        'age': 16
    },
]

# for x in animals:
#     print(x)
#     print(f"{x['owner']} has {x['type']} of age {x['age']}")




# SET, Tuple, string

customers = ['Faisal', 'Waseem', 'Saleem']
ages = [33, 55, 66]

for item in  enumerate(customers):
    # type(item) #?
    print(item)
    print('index -> ', item[0])
    print('value -> ', item[1])

for ind, val in enumerate(customers):
    # type(x) #?
    print(ind)
    print(val)
    print(ages[ind])