with open("input.txt") as f:
    data = f.read().splitlines()
    
    
x_lookup = {"R": 1, "L": -1, "U": 0, "D": 0}
y_lookup = {"U": 1, "D": -1, "L": 0, "R": 0} 
    
visited = set([(0, 0)])
head = [0, 0]
tail = [0, 0]

for line in data:
    direction, amount = line.split()
    amount = int(amount)
    
    for _ in range(amount):
        
        head[0] += x_lookup[direction]
        head[1] += y_lookup[direction]
        
        dx = head[0] - tail[0]
        dy = head[1] - tail[1]
        
        if abs(dx) > 1 or abs(dy) > 1:
            
            if dx == 0:
                tail[1] += dy // 2
            
            elif dy == 0:
                tail[0] += dx // 2
                
            else:
                tail[0] += (1 if dx > 0 else -1)
                tail[1] += (1 if dy > 0 else -1)
                
        visited.add(tuple(tail))
        
        
print(len(visited))
# 5735
