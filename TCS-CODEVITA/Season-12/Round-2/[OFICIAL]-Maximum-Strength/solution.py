# Problem: Maximum Strength (Shark-infested island escape)
# Algorithm: Dynamic Programming / Dijkstra over grid
# Time Complexity: O(R * C log(R * C))
# Space Complexity: O(R * C)

import sys
import heapq

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
        
    initial_strength = int(input_data[idx])
    
    # Dijkstra to maximize remaining strength or minimize damage
    # Damage incurred is grid[r][c]
    dist = [[float('inf')] * C for _ in range(R)]
    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]
    
    while pq:
        d, r, c = heapq.heappop(pq)
        if d > dist[r][c]:
            continue
        if r == R - 1 and c == C - 1:
            break
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                nd = d + grid[nr][nc]
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(pq, (nd, nr, nc))
                    
    min_damage = dist[R-1][C-1]
    if initial_strength >= min_damage:
        print(initial_strength - min_damage)
    else:
        print("Not Possible")

if __name__ == "__main__":
    solve()
