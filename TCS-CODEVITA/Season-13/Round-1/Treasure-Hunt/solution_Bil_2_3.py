def solve():
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]
    start_x, start_y = map(int, input().split())
    pearl, platinum, gold, diamond = map(int, input().split())
    k = int(input())
    
    values = {'$': pearl, '*': platinum, '%': gold, '+': diamond}
    
    def is_stable(r, c):
        return r == n - 1 or (r + 1 < n and grid[r + 1][c] == '#')
    
    memo = {}
    
    def dfs(r, c, steps, visited):
        if steps > k:
            return 0
        
        state = (r, c, steps, tuple(sorted(visited)))
        if state in memo:
            return memo[state]
        
        max_val = 0
        
        # If current position is stable and not last row, it's a valid end
        if is_stable(r, c) and r != n - 1:
            current_treasure = sum(values.get(grid[vr][vc], 0) for vr, vc in visited)
            max_val = current_treasure
        
        if steps == k:
            memo[state] = max_val
            return max_val
        
        # Try moves: left, right, up
        directions = [(0, -1), (0, 1)]  # left, right
        
        # Add up moves (can climb multiple levels)
        for up_r in range(r - 1, -1, -1):
            if grid[up_r][c] != '#':
                directions.append((up_r - r, 0))
            else:
                break
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#':
                new_visited = set(visited)
                
                # Add current cell to visited
                new_visited.add((nr, nc))
                
                # Apply gravity
                final_r = nr
                while not is_stable(final_r, nc) and final_r < n - 1:
                    final_r += 1
                    new_visited.add((final_r, nc))
                
                result = dfs(final_r, nc, steps + 1, new_visited)
                max_val = max(max_val, result)
        
        memo[state] = max_val
        return max_val
    
    # Start with initial position in visited set
    initial_visited = {(start_x, start_y)}
    result = dfs(start_x, start_y, 0, initial_visited)
    print(result)

solve()
