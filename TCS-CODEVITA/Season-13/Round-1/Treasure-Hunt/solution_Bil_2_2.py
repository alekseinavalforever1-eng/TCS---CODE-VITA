n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
x, y = map(int, input().split())
pearl, platinum, gold, diamond = map(int, input().split())
k = int(input())

val = {'$': pearl, '*': platinum, '%': gold, '+': diamond}

def stable(r, c):
    return r == n - 1 or (r + 1 < n and grid[r + 1][c] == '#')

def dfs(r, c, steps, treasure):
    if steps > k:
        return 0
    
    best = treasure if stable(r, c) and r < n - 1 else 0
    
    if steps == k:
        return best
    
    # Left move
    if c > 0 and grid[r][c - 1] != '#':
        nr, nc = r, c - 1
        new_treasure = treasure + val.get(grid[nr][nc], 0)
        while not stable(nr, nc) and nr < n - 1:
            nr += 1
            new_treasure += val.get(grid[nr][nc], 0)
        best = max(best, dfs(nr, nc, steps + 1, new_treasure))
    
    # Right move
    if c < m - 1 and grid[r][c + 1] != '#':
        nr, nc = r, c + 1
        new_treasure = treasure + val.get(grid[nr][nc], 0)
        while not stable(nr, nc) and nr < n - 1:
            nr += 1
            new_treasure += val.get(grid[nr][nc], 0)
        best = max(best, dfs(nr, nc, steps + 1, new_treasure))
    
    # Up moves - can reach any treasure cell above (climbing through rocks is free)
    for nr in range(r - 1, -1, -1):
        if grid[nr][c] != '#':  # Can land on this treasure cell
            new_treasure = treasure + val.get(grid[nr][c], 0)
            final_r = nr
            while not stable(final_r, c) and final_r < n - 1:
                final_r += 1
                new_treasure += val.get(grid[final_r][c], 0)
            best = max(best, dfs(final_r, c, steps + 1, new_treasure))
    
    return best

print(dfs(x, y, 0, val.get(grid[x][y], 0)))
