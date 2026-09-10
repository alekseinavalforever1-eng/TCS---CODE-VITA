# Problem: Island Perimeter & Area
# Algorithm: Grid Traversal (DFS / BFS)
# Time Complexity: O(R * C)
# Space Complexity: O(R * C)

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    R = int(input_data[0])
    C = int(input_data[1])
    grid = []
    idx = 2
    for _ in range(R):
        grid.append([int(x) for x in input_data[idx:idx+C]])
        idx += C
        
    perimeter = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= R or nc < 0 or nc >= C or grid[nr][nc] == 0:
                        perimeter += 1
                        
    print(perimeter)

if __name__ == "__main__":
    solve()
