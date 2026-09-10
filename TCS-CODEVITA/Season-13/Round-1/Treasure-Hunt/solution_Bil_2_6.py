import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
x, y = map(int, input().split())
pearl, platinum, gold, diamond = map(int, input().split())
k = int(input())

val = {'$': pearl, '*': platinum, '%': gold, '+': diamond}

def stable(r, c):
    return r == n - 1 or (r + 1 < n and grid[r + 1][c] == '#')

dp = {}

def solve(r, c, steps):
    if (r, c, steps) in dp:
        return dp[(r, c, steps)]
    
    if steps > k:
        return 0
    
    current_val = val.get(grid[r][c], 0)
    result = current_val if stable(r, c) and r < n - 1 else 0
    
    if steps == k:
        dp[(r, c, steps)] = result
        return result
    
    # Try all moves
    moves = []
    
    # Left and Right
    for dc in [-1, 1]:
        nc = c + dc
        if 0 <= nc < m and grid[r][nc] != '#':
            nr = r
            while not stable(nr, nc) and nr < n - 1:
                nr += 1
            moves.append((nr, nc))
    
    # Up - all reachable positions
    for nr in range(r - 1, -1, -1):
        if grid[nr][c] != '#':
            final_r = nr
            while not stable(final_r, c) and final_r < n - 1:
                final_r += 1
            moves.append((final_r, c))
    
    for nr, nc in moves:
        result = max(result, current_val + solve(nr, nc, steps + 1))
    
    dp[(r, c, steps)] = result
    return result

print(solve(x, y, 0))
