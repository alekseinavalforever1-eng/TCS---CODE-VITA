import heapq, math

def solve():
    M = int(input().strip())
    dist = [list(map(int, input().split())) for _ in range(M)]
    employees = [0] + list(map(int, input().split()))
    capacity = int(input().strip())

    graph = [[] for _ in range(M)]
    for i in range(M):
        for j in range(M):
            if i != j:
                graph[i].append((dist[i][j], j))

    def dijkstra(src):
        d = [float('inf')] * M
        d[src] = 0
        pq = [(0, src)]
        while pq:
            cost, u = heapq.heappop(pq)
            if cost > d[u]:
                continue
            for w, v in graph[u]:
                if d[v] > cost + w:
                    d[v] = cost + w
                    heapq.heappush(pq, (d[v], v))
        return d

    shortest = dijkstra(0)
    parent = [-1] * M
    for i in range(1, M):
        for j in range(M):
            if shortest[j] + dist[j][i] == shortest[i]:
                parent[i] = j
                break

    children = [[] for _ in range(M)]
    for i in range(1, M):
        children[parent[i]].append(i)

    buses = 0
    def dfs(u):
        nonlocal buses
        load = employees[u]
        for v in children[u]:
            load += dfs(v)
        buses += math.ceil(load / capacity)
        return 0
    dfs(0)
    print(buses)

solve()
