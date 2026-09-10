n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
x, y = map(int, input().split())
pearl, platinum, gold, diamond = map(int, input().split())
k = int(input())

val = {'$': pearl, '*': platinum, '%': gold, '+': diamond}

def stable(r, c):
    return r == n - 1 or (r + 1 < n and grid[r + 1][c] == '#')

def dfs(r, c, steps, path_treasure):
    if steps > k:
        return 0
    
    best = path_treasure if stable(r, c) and r < n - 1 else 0
    
    if steps == k:
        return best
    
    # Try moves: left, right, up
    for dr, dc in [(0, -1), (0, 1), (-1, 0)]:
        if dr == -1:  # Up move - try all levels
            for nr in range(r - 1, -1, -1):
                if 0 <= nr < n and 0 <= c < m and grid[nr][c] != '#':
                    new_treasure = path_treasure + val.get(grid[nr][c], 0)
                    
                    # Apply gravity
                    final_r = nr
                    while not stable(final_r, c) and final_r < n - 1:
                        final_r += 1
                        new_treasure += val.get(grid[final_r][c], 0)
                    
                    best = max(best, dfs(final_r, c, steps + 1, new_treasure))
                else:
                    break
        else:  # Left/right move
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#':
                new_treasure = path_treasure + val.get(grid[nr][nc], 0)
                
                # Apply gravity
                final_r = nr
                while not stable(final_r, nc) and final_r < n - 1:
                    final_r += 1
                    new_treasure += val.get(grid[final_r][nc], 0)
                
                best = max(best, dfs(final_r, nc, steps + 1, new_treasure))
    
    return best

print(dfs(x, y, 0, val.get(grid[x][y], 0)))
