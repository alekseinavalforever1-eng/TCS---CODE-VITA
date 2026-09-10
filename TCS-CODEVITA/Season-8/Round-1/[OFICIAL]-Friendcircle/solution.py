# Problem: Friend Circle (Connected Components)
# Algorithm: Disjoint Set Union (DSU) / BFS
# Time Complexity: O(N^2)
# Space Complexity: O(N)

import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    lines = [l.strip() for l in input_data if l.strip()]
    if not lines:
        return
    N = int(lines[0])
    adj = []
    for i in range(1, N + 1):
        adj.append(list(map(int, lines[i].split())))
        
    visited = [False] * N
    circles = 0
    
    def dfs(node):
        visited[node] = True
        for neighbor in range(N):
            if adj[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
                
    for i in range(N):
        if not visited[i]:
            dfs(i)
            circles += 1
            
    print(circles)

if __name__ == "__main__":
    solve()
