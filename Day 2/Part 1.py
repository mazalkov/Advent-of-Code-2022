with open("input.txt") as f:
    lines = f.read().splitlines()


convert = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

winner = {
    "X": "Z",
    "Y": "X",
    "Z": "Y",
}

first_score = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

second_score = {
    "lose": 0,
    "draw": 3,
    "win": 6,
}

total = 0

for line in lines:
    player = line[-1]
    opponent = convert[line[0]]
    
    total += first_score[player]

    if winner[player] == opponent:
        total += second_score["win"]

    elif winner[opponent] == player:
        total += second_score["lose"]

    else:
        total += second_score["draw"]


print(total)
# 11603
