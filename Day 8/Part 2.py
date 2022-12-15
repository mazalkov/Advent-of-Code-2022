with open("input.txt") as f:
    data = f.read().splitlines()


grid = [list(map(int, line)) for line in data]

ROWS, COLS = len(grid), len(grid[0])

highest = 1

for r in range(ROWS):
    for c in range(COLS):
        cur = grid[r][c]

        left, right, up, down = 0, 0, 0, 0

        for x in range(c-1, -1, -1):
            left += 1
            if cur <= grid[r][x]:
                break

        for x in range(c+1, COLS):
            right += 1
            if cur <= grid[r][x]:
                break

        for y in range(r-1, -1, -1):
            up += 1
            if cur <= grid[y][c]:
                break

        for y in range(r+1, ROWS):
            down += 1
            if cur <= grid[y][c]:
                break

        score = left*right*up*down
        highest = max(score, highest)
            
        
print(highest)
# 313200
