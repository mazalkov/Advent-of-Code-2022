with open("input.txt") as f:
    data = f.read().strip()
    

for i, char in enumerate(data):
  
    chunk = data[i:i+4]
    if len(set(chunk)) == 4:
        # add 4 because
        # we need the
        # end chunk index
        print(i+4)
        
        break
        

# 1896
