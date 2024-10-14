dictt = {1: 2, 
       2: 3.5,
    3: {'a': False,
        'b': 354,
        'c': 'yo',
        'd': 2.27
       },
    4: 'Hello',
    5: True,
}

mass = []

for key, value in dictt.items():
    if type(value) == dict:
        for key1, value1 in value.items():
            mass.append(type(value1))
    else:
        mass.append(type(value)) 
    

print(mass)
