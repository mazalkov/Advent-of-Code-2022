with open("input.txt") as f:
    data = f.read().split()
    
    
total = 0

for line in data:
    first, second = line.split(",")
    x1, x2 = first.split("-")
    y1, y2 = second.split("-")
    
    x_range = range(int(x1), int(x2)+1)
    y_range = range(int(y1), int(y2)+1)
    
    # if the set of their intersections exists
    if set(x_range).intersection(y_range):
        total += 1
        
        
print(total)
# 806
