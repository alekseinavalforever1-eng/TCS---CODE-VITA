def solve():
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    start_x, start_y = map(int, input().split())
    pearl, platinum, gold, diamond = map(int, input().split())
    k = int(input())
    
    values = {'$': pearl, '*': platinum, '%': gold, '+': diamond}
    
    def is_stable(r, c):
        return r == n - 1 or (r + 1 < n and grid[r + 1][c] == '#')
    
    memo = {}
    
    def dfs(r, c, steps):
        if (r, c, steps) in memo:
            return memo[(r, c, steps)]
        
        if steps > k:
            return 0
        
        # Current treasure value
        current_treasure = values.get(grid[r][c], 0)
        
        # If this is a valid ending position, record the treasure
        best = current_treasure if (is_stable(r, c) and r != n - 1) else 0
        
        if steps == k:
            memo[(r, c, steps)] = best
            return best
        
        # Try all moves
        moves = []
        
        # Left
        if c > 0 and grid[r][c - 1] != '#':
            moves.append((r, c - 1))
        
        # Right
        if c < m - 1 and grid[r][c + 1] != '#':
            moves.append((r, c + 1))
        
        # Up - try all reachable levels
        for up_r in range(r - 1, -1, -1):
            if grid[up_r][c] != '#':
                moves.append((up_r, c))
            else:
                break
        
        for nr, nc in moves:
            # Calculate treasure from this move
            move_treasure = current_treasure + values.get(grid[nr][nc], 0)
            
            # Apply gravity and collect treasures during fall
            final_r = nr
            while not is_stable(final_r, nc) and final_r < n - 1:
                final_r += 1
                move_treasure += values.get(grid[final_r][nc], 0)
            
            # Recursively explore from final position
            future_treasure = dfs(final_r, nc, steps + 1)
            
            # The total treasure is current + move treasures + future treasures - current
            # (subtract current because it's counted in future_treasure too)
            total_treasure = move_treasure + future_treasure - values.get(grid[final_r][nc], 0)
            
            best = max(best, total_treasure)
        
        memo[(r, c, steps)] = best
        return best
    
    result = dfs(start_x, start_y, 0)
    print(result)

solve()
