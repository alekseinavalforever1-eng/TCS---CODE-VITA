from collections import deque

def solve():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(input().strip()))
    
    start_x, start_y = map(int, input().split())
    pearl, platinum, gold, diamond = map(int, input().split())
    k = int(input())
    
    values = {'$': pearl, '*': platinum, '%': gold, '+': diamond}
    
    def is_stable(r, c):
        if r == n - 1:  # Last row is stable
            return True
        if r + 1 < n and grid[r + 1][c] == '#':  # Rock beneath
            return True
        return False
    
    # BFS with state: (row, col, steps, treasure_collected, visited_cells)
    queue = deque()
    
    # Start with initial treasure
    start_treasure = values.get(grid[start_x][start_y], 0)
    start_visited = {(start_x, start_y)}
    queue.append((start_x, start_y, 0, start_treasure, frozenset(start_visited)))
    
    max_treasure = 0
    seen_states = set()
    
    while queue:
        row, col, steps, treasure, visited_cells = queue.popleft()
        
        # Create state key for memoization
        state_key = (row, col, steps, visited_cells)
        if state_key in seen_states:
            continue
        seen_states.add(state_key)
        
        # Check if this is a valid ending position
        if is_stable(row, col) and row != n - 1:  # Stable but not last row
            max_treasure = max(max_treasure, treasure)
        
        # If we've used all steps, continue
        if steps >= k:
            continue
        
        # Try all possible moves: left, right, up
        directions = [(0, -1), (0, 1), (-1, 0)]  # left, right, up
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check bounds and that it's not a rock
            if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] != '#':
                new_visited = set(visited_cells)
                new_treasure = treasure
                
                # Move to the new position
                current_row = new_row
                
                # Collect treasure from new position if not visited
                if (current_row, new_col) not in new_visited:
                    if grid[current_row][new_col] in values:
                        new_treasure += values[grid[current_row][new_col]]
                    new_visited.add((current_row, new_col))
                
                # Apply gravity if the position is unstable
                while not is_stable(current_row, new_col) and current_row < n - 1:
                    current_row += 1
                    # Collect treasure during fall if not visited
                    if (current_row, new_col) not in new_visited:
                        if grid[current_row][new_col] in values:
                            new_treasure += values[grid[current_row][new_col]]
                        new_visited.add((current_row, new_col))
                
                # Add new state to queue
                queue.append((current_row, new_col, steps + 1, new_treasure, frozenset(new_visited)))
    
    print(max_treasure)

solve()
