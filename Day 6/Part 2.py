with open("input.txt") as f:
    data = f.read().strip()
    

for i, char in enumerate(data):
    chunk = data[i:i+14]
    if len(set(chunk)) == 14:
        # add 14 because
        # we need the
        # end chunk index
        print(i+14)
        break
