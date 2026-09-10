def solve():
    S = int(input().strip())
    grid = [list(input().strip()) for _ in range(S)]
    overlaps = 0
    for i in range(1, S-1):
        for j in range(1, S-1):
            if grid[i][j] in ("1", "2"):
                ch = grid[i][j]
                other = "2" if ch == "1" else "1"
                if (grid[i-1][j] == ch and grid[i+1][j] == ch and 
                    grid[i][j-1] == other and grid[i][j+1] == other):
                    overlaps += 1
                elif (grid[i][j-1] == ch and grid[i][j+1] == ch and 
                      grid[i-1][j] == other and grid[i+1][j] == other):
                    overlaps += 1
    if overlaps % 2 != 0:
        print("Impossible")
    else:
        if overlaps > 0:
            print(overlaps)
        else:
            print("Impossible")

solve()
