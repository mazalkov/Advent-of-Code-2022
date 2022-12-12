from string import ascii_lowercase, ascii_uppercase

with open("input.txt") as f:
    data = f.read().split()
  
  
lower_lookup = dict(zip(ascii_lowercase, range(1, 27)))
upper_lookup = dict(zip(ascii_uppercase, range(27, 53)))

# combine the dicts together:
lookup = {**lower_lookup, **upper_lookup}

total = 0

for line in data:
    first_half = line[:len(line)//2]
    second_half = line[len(line)//2:]
  
    shared = set(first_half).intersection(set(second_half))
    total += lookup[shared.pop()]
  
  
print(total)
# 7878
