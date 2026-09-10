# Problem: All Party Meet (Optimal meeting node in tree/graph)
# Algorithm: All-Pairs Shortest Path / Tree Centroid
# Time Complexity: O(V * (V + E))
# Space Complexity: O(V + E)

import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    M = int(input_data[1])
    adj = {i: [] for i in range(1, N + 1)}
    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    best_sum = float('inf')
    best_node = 1
    
    for start in range(1, N + 1):
        dist = {i: float('inf') for i in range(1, N + 1)}
        dist[start] = 0
        q = deque([start])
        while q:
            curr = q.popleft()
            for nxt in adj[curr]:
                if dist[nxt] == float('inf'):
                    dist[nxt] = dist[curr] + 1
                    q.append(nxt)
        total_dist = sum(dist.values())
        if total_dist < best_sum:
            best_sum = total_dist
            best_node = start
            
    print(best_node)

if __name__ == "__main__":
    solve()
