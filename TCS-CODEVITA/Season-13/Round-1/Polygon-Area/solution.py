def length(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

def polygon_area(points):
    n = len(points)
    area = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def solve():
    n = int(input().strip())
    sticks = []
    lengths = []
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        sticks.append(((x1, y1), (x2, y2)))
        lengths.append(length(x1, y1, x2, y2))
    
    # Try to find polygon cycle
    from collections import defaultdict, deque
    graph = defaultdict(list)
    for i, (p1, p2) in enumerate(sticks):
        graph[p1].append((p2, i))
        graph[p2].append((p1, i))
    
    visited_edges = set()
    polygon = []
    
    def dfs(start, current, path, used_edges):
        if len(path) >= 3 and current == start:
            return path
        for nxt, idx in graph[current]:
            if idx not in used_edges:
                new_used = used_edges | {idx}
                res = dfs(start, nxt, path + [nxt], new_used)
                if res: return res
        return None
    
    closed_polygon = None
    for p in graph:
        res = dfs(p, p, [p], set())
        if res:
            closed_polygon = res[:-1]
            break
    
    if not closed_polygon:
        print("No")
        return
    
    print("Yes")
    
    # Compute perimeter of polygon
    perimeter = 0
    for i in range(len(closed_polygon)):
        x1, y1 = closed_polygon[i]
        x2, y2 = closed_polygon[(i + 1) % len(closed_polygon)]
        perimeter += length(x1, y1, x2, y2)
    
    polygon_area_val = polygon_area(closed_polygon)
    
    used_edges = set()
    for i, (p1, p2) in enumerate(sticks):
        for j in range(len(closed_polygon)):
            a, b = closed_polygon[j], closed_polygon[(j+1) % len(closed_polygon)]
            if (p1 == a and p2 == b) or (p1 == b and p2 == a):
                used_edges.add(i)
    
    leftover = 0
    for i in range(n):
        if i not in used_edges:
            leftover += lengths[i]
    
    if leftover >= perimeter:
        print("Yes")
    else:
        print("No")
    
    print(f"{polygon_area_val:.2f}")
