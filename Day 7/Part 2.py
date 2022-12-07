with open("input.txt") as f:
    lines = f.read().splitlines()
    

folders = {}
stack = []

for line in lines:
    size = 0
    command = line.split(" ")
    
    if ("dir" not in command) and ("ls" not in command):

        if "cd" in command:
            if ".." in command:
                stack.pop()
            
            else:
                try:
                    join = "" if stack[-1] == "/" else "/"
                    stack.append(f"{stack[-1]}{join}{command[2]}")
                except:
                    stack.append(command[2])
                    
        else:
            size = int(command[0])
            
        if size:
            for folder in stack:
                folders[folder] = folders.get(folder, 0) + size
                

total_size = folders["/"]
required = 30000000 - (70000000 - total_size)

print(min([total for total in folders.values() if total >= required]))
# 366028
