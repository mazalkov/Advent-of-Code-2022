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
                # this could be made way better but it works
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
                
                
print(sum([total for total in folders.values() if total <= 100000]))
# 1086293
