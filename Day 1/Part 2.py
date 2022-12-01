with open("input.txt") as f:
    lines = f.read().splitlines()


sums = []
running_total = 0
for n in lines:
    if n != "":
        running_total += int(n)
    else:
        sums.append(running_total)
        running_total = 0


sums.sort()
print(sum(sums[-3:]))
