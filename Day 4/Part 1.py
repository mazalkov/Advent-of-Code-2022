with open("input.txt") as f:
    data = f.read().split()
    
    
total = 0

for line in data:
    first, second = line.split(",")
    x1, x2 = first.split("-")
    y1, y2 = second.split("-")
    
    if int(x1) <= int(y1) and int(x2) >= int(y2):
        total += 1
        
    elif int(y1) <= int(x1) and int(y2) >= int(x2):
        total += 1
        
        
print(total)
# 413
