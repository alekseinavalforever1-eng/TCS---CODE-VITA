# Problem: Between Devil and Deep Sea (Multi-source BFS + Shortest Path)
import sys
from collections import deque

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    R, C, D = map(int, lines[0].split())
    grid = [list(lines[i+1]) for i in range(R)]
    
    # BFS from all Devils to compute hazard distance
    dist_devil = [[float('inf')] * C for _ in range(R)]
    q = deque()
    start, end = None, None
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'D':
                dist_devil[r][c] = 0
                q.append((r, c))
            elif grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)
                
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#' and dist_devil[nr][nc] == float('inf'):
                dist_devil[nr][nc] = dist_devil[r][c] + 1
                q.append((nr, nc))
                
    # BFS for player
    if dist_devil[start[0]][start[1]] <= D:
        print(-1)
        return
        
    dist_player = [[-1] * C for _ in range(R)]
    dist_player[start[0]][start[1]] = 0
    pq = deque([start])
    while pq:
        r, c = pq.popleft()
        if (r, c) == end:
            print(dist_player[r][c])
            return
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#' and dist_player[nr][nc] == -1:
                if dist_devil[nr][nc] > D:
                    dist_player[nr][nc] = dist_player[r][c] + 1
                    pq.append((nr, nc))
    print(-1)

if __name__ == "__main__":
    solve()
