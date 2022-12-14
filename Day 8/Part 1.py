with open("input.txt") as f:
    data = f.read().splitlines()


grid = [list(map(int, line)) for line in data]

ROWS, COLS = len(grid), len(grid[0])

total = 0

for r in range(ROWS):
    for c in range(COLS):
        cur = grid[r][c]

        left = all(grid[r][y] < cur for y in range(c))
        right = all(grid[r][y] < cur for y in range(c+1, COLS))
        up = all(grid[x][c] < cur for x in range(r))
        down = all(grid[x][c] < cur for x in range(r+1, ROWS))

        if any((left, right, up, down)):
            total += 1


print(total)
# 1676
