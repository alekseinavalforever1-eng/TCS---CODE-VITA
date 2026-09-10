n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
x, y = map(int, input().split())
pearl, platinum, gold, diamond = map(int, input().split())
k = int(input())

val = {'$': pearl, '*': platinum, '%': gold, '+': diamond}

def stable(r, c):
    return r == n - 1 or (r + 1 < n and grid[r + 1][c] == '#')

memo = {}

def dfs(r, c, steps):
    if (r, c, steps) in memo:
        return memo[(r, c, steps)]
    
    if steps > k:
        return 0
    
    # Current treasure value
    current_val = val.get(grid[r][c], 0)
    
    # If this is a valid ending position
    best = current_val if stable(r, c) and r < n - 1 else 0
    
    if steps == k:
        memo[(r, c, steps)] = best
        return best
    
    # Try moves: left, right, up
    for dr, dc in [(0, -1), (0, 1), (-1, 0)]:
        if dr == -1:  # Up move - try all reachable levels
            for nr in range(r - 1, -1, -1):
                if grid[nr][c] != '#':
                    # Calculate final position after gravity
                    final_r = nr
                    while not stable(final_r, c) and final_r < n - 1:
                        final_r += 1
                    
                    # Get treasure from future path
                    future_val = dfs(final_r, c, steps + 1)
                    best = max(best, current_val + future_val)
        else:  # Left/right move
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#':
                # Calculate final position after gravity
                final_r = nr
                while not stable(final_r, nc) and final_r < n - 1:
                    final_r += 1
                
                # Get treasure from future path
                future_val = dfs(final_r, nc, steps + 1)
                best = max(best, current_val + future_val)
    
    memo[(r, c, steps)] = best
    return best

print(dfs(x, y, 0))
