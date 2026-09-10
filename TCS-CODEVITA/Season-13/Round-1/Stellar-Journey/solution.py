from collections import deque

# Check if point lies on a segment
def point_on_segment(pt, seg):
    (x1,y1),(x2,y2) = seg
    if x1 == x2:  # vertical
        return pt[0] == x1 and min(y1, y2) <= pt[1] <= max(y1, y2)
    elif y1 == y2:  # horizontal
        return pt[1] == y1 and min(x1, x2) <= pt[0] <= max(x1, x2)
    else:  # diagonal
        dx = x2 - x1
        dy = y2 - y1
        if dx == 0 or dy == 0:
            return False
        return (pt[0] - x1) * dy == (pt[1] - y1) * dx and min(x1,x2) <= pt[0] <= max(x1,x2) and min(y1,y2) <= pt[1] <= max(y1,y2)

# Check if point is in star
def point_in_star(pt, star):
    return any(point_on_segment(pt, seg) for seg in star)

# Check if two segments intersect (bounding-box approximation)
def intersects(seg1, seg2):
    (x1,y1),(x2,y2) = seg1
    (x3,y3),(x4,y4) = seg2
    if max(x1,x2) < min(x3,x4) or max(x3,x4) < min(x1,x2):
        return False
    if max(y1,y2) < min(y3,y4) or max(y3,y4) < min(y1,y2):
        return False
    return True

# Read input
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
segments = [((x1,y1),(x2,y2)) for x1,y1,x2,y2 in segments]
start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))

# Step 1: Cluster segments into stars
stars = []
visited = [False]*n

for i in range(n):
    if visited[i]:
        continue
    queue = [i]
    star = []
    visited[i] = True
    while queue:
        idx = queue.pop()
        star.append(segments[idx])
        for j in range(n):
            if not visited[j] and intersects(segments[idx], segments[j]):
                visited[j] = True
                queue.append(j)
    stars.append(star)

# Step 2: Find stars containing start and end points
start_star = next((i for i, s in enumerate(stars) if point_in_star(start, s)), -1)
end_star = next((i for i, s in enumerate(stars) if point_in_star(end, s)), -1)

if start_star == -1 or end_star == -1:
    print("Impossible")
    exit()

# Step 3: Build connectivity graph
graph = {i: set() for i in range(len(stars))}
for i in range(len(stars)):
    for j in range(i+1, len(stars)):
        if any(intersects(seg1, seg2) for seg1 in stars[i] for seg2 in stars[j]):
            graph[i].add(j)
            graph[j].add(i)

# Step 4: BFS for minimum stars
queue = deque([(start_star, 1)])
visited_stars = set()

while queue:
    current, count = queue.popleft()
    if current == end_star:
        print(count)
        exit()
    visited_stars.add(current)
    for neighbor in graph.get(current, []):
        if neighbor not in visited_stars:
            queue.append((neighbor, count+1))

print("Impossible")
