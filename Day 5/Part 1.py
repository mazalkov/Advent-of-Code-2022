stack1 = ['W', 'M', 'L', 'F']
stack2 = ['B', 'Z', 'V', 'M', 'F']
stack3 = ['H', 'V', 'R', 'S', 'L', 'Q']
stack4 = ['F', 'S', 'V', 'Q', 'P', 'M', 'T', 'J']
stack5 = ['W', 'S', 'L']
stack6 = ['F', 'V', 'P', 'M', 'R', 'J', 'W']
stack7 = ['J', 'Q', 'C', 'P', 'N', 'R', 'F']
stack8 = ['V', 'H', 'P', 'S', 'Z', 'W', 'R', 'B']
stack9 = ['B', 'M', 'J', 'C', 'G', 'H', 'Z', 'W']

stacks = [stack1, stack2, stack3, stack4, stack5, 
          stack6, stack7, stack8, stack9]


moves = []

for line in open("input.txt"):
    # could stop checking this after
    # the initial stack definitions,
    # but it's fast enough without
    if "move" in line:
        move = line.strip().split()
        quantity = int(move[1])
        from_stack = int(move[3])
        to_stack = int(move[5])
        
        for _ in range(quantity):
            # subtract 1 from indices as stacks start at 1
            removed = stacks[from_stack-1].pop()
            stacks[to_stack-1].append(removed)
        

res = ""
for stack in stacks:
    res += stack[-1]
    
print(res)
