# Problem: Image Segmentation (Connected Components in Binary Grid)
# Algorithm: Flood-fill / Multi-source BFS
# Time Complexity: O(R * C)
# Space Complexity: O(R * C)

import sys
from collections import deque

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
        
    visited = [[False] * C for _ in range(R)]
    segments = 0
    
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1 and not visited[r][c]:
                segments += 1
                q = deque([(r, c)])
                visited[r][c] = True
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                            
    print(segments)

if __name__ == "__main__":
    solve()
