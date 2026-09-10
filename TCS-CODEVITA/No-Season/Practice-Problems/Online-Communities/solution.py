# Problem: Online Communities (Disjoint Set Union)
import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.max_size = 1
        
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
        
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            self.max_size = max(self.max_size, self.size[root_i])

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    N = int(next(it))
    Q = int(next(it))
    dsu = DSU(N)
    for _ in range(Q):
        op = int(next(it))
        if op == 1:
            u, v = int(next(it)), int(next(it))
            dsu.union(u, v)
        elif op == 2:
            u = int(next(it))
            print(dsu.size[dsu.find(u)])
        elif op == 3:
            print(dsu.max_size)

if __name__ == "__main__":
    solve()
