from string import ascii_lowercase, ascii_uppercase

with open("input.txt") as f:
    data = f.read().split()
  
  
lower_lookup = dict(zip(ascii_lowercase, range(1, 27)))
upper_lookup = dict(zip(ascii_uppercase, range(27, 53)))

# combine the dicts together:
lookup = {**lower_lookup, **upper_lookup}

total = 0

for index in range(0, len(data)-1, 3):
    
    first = data[index]
    second = data[index+1]
    third = data[index+2]
    
    shared_first_second = set(first).intersection(set(second))
    shared_second_third = set(second).intersection(set(third))
    shared = shared_second_third.intersection(shared_first_second)
    
    total += lookup[shared.pop()]
    
    
print(total)
# 2760
