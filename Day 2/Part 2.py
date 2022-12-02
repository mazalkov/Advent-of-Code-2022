with open("input.txt") as f:
    lines = f.read().splitlines()


points = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}


losses = {
    "A": 3,
    "B": 1,
    "C": 2,
}


draws = {
    "A": 1,
    "B": 2,
    "C": 3,
}


wins = {
    "A": 2,
    "B": 3,
    "C": 1,
}


lookup = {
    "X": losses,
    "Y": draws,
    "Z": wins,
}


total = 0

for line in lines:
    player = line[-1]
    opponent = line[0]

    # bad use of dict->dict indexing
    # but gets the first score added
    total += lookup[player][opponent]
    
    # now add the points from L/D/W
    total += points[player]


print(total)
# 12725
