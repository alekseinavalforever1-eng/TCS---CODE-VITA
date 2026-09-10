n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
x, y = map(int, input().split())
pearl, platinum, gold, diamond = map(int, input().split())
k = int(input())

val = {'$': pearl, '*': platinum, '%': gold, '+': diamond}

def stable(r, c):
    return r == n - 1 or (r + 1 < n and grid[r + 1][c] == '#')

best = 0

def dfs(r, c, steps, treasure, visited):
    global best
    
    if steps > k:
        return
    
    if stable(r, c) and r < n - 1:
        best = max(best, treasure)
    
    if steps == k:
        return
    
    # Left
    if c > 0 and grid[r][c - 1] != '#' and (r, c - 1) not in visited:
        new_visited = visited | {(r, c - 1)}
        new_treasure = treasure + val.get(grid[r][c - 1], 0)
        nr, nc = r, c - 1
        while not stable(nr, nc) and nr < n - 1:
            nr += 1
            if (nr, nc) not in new_visited:
                new_treasure += val.get(grid[nr][nc], 0)
                new_visited = new_visited | {(nr, nc)}
        dfs(nr, nc, steps + 1, new_treasure, new_visited)
    
    # Right
    if c < m - 1 and grid[r][c + 1] != '#' and (r, c + 1) not in visited:
        new_visited = visited | {(r, c + 1)}
        new_treasure = treasure + val.get(grid[r][c + 1], 0)
        nr, nc = r, c + 1
        while not stable(nr, nc) and nr < n - 1:
            nr += 1
            if (nr, nc) not in new_visited:
                new_treasure += val.get(grid[nr][nc], 0)
                new_visited = new_visited | {(nr, nc)}
        dfs(nr, nc, steps + 1, new_treasure, new_visited)
    
    # Up
    for nr in range(r - 1, -1, -1):
        if grid[nr][c] != '#' and (nr, c) not in visited:
            new_visited = visited | {(nr, c)}
            new_treasure = treasure + val.get(grid[nr][c], 0)
            final_r = nr
            while not stable(final_r, c) and final_r < n - 1:
                final_r += 1
                if (final_r, c) not in new_visited:
                    new_treasure += val.get(grid[final_r][c], 0)
                    new_visited = new_visited | {(final_r, c)}
            dfs(final_r, c, steps + 1, new_treasure, new_visited)

start_treasure = val.get(grid[x][y], 0)
dfs(x, y, 0, start_treasure, {(x, y)})
print(best)
