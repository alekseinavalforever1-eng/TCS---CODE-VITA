from collections import defaultdict, deque
import math

n = int(input())
segments = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    segments.append((x1, y1, x2, y2))

source = tuple(map(int, input().split()))
dest = tuple(map(int, input().split()))

def intersect(s1, s2):
    x1, y1, x2, y2 = s1
    x3, y3, x4, y4 = s2
    denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if abs(denom) < 1e-10:
        return None
    t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / denom
    u = -((x1-x2)*(y1-y3) - (y1-y2)*(x1-x3)) / denom
    if 0 <= t <= 1 and 0 <= u <= 1:
        return (round(x1 + t*(x2-x1), 6), round(y1 + t*(y2-y1), 6))
    return None

stars = defaultdict(set)
for i in range(n):
    for j in range(i+1, n):
        pt = intersect(segments[i], segments[j])
        if pt:
            stars[pt].add(i)
            stars[pt].add(j)

stars = {k: v for k, v in stars.items() if len(v) >= 2}

def find_star(point):
    px, py = point
    best_star = None
    min_dist = float('inf')
    
    for center in stars:
        # Check if on star center
        if abs(px - center[0]) < 0.01 and abs(py - center[1]) < 0.01:
            return center
        
        # Check if on any segment
        for seg_id in stars[center]:
            x1, y1, x2, y2 = segments[seg_id]
            if (min(x1,x2) - 0.01 <= px <= max(x1,x2) + 0.01 and 
                min(y1,y2) - 0.01 <= py <= max(y1,y2) + 0.01):
                cross = (py - y1) * (x2 - x1) - (px - x1) * (y2 - y1)
                if abs(cross) < 0.1:
                    return center
        
        # Find closest star as fallback
        dist = math.sqrt((px - center[0])**2 + (py - center[1])**2)
        if dist < min_dist:
            min_dist = dist
            best_star = center
    
    # Return closest star if within reasonable distance
    return best_star if min_dist < 20 else None

def can_connect(star1, star2):
    max_reach1 = max(math.sqrt((segments[i][2]-segments[i][0])**2 + (segments[i][3]-segments[i][1])**2) 
                     for i in stars[star1])
    max_reach2 = max(math.sqrt((segments[i][2]-segments[i][0])**2 + (segments[i][3]-segments[i][1])**2) 
                     for i in stars[star2])
    center_dist = math.sqrt((star1[0]-star2[0])**2 + (star1[1]-star2[1])**2)
    return center_dist <= (max_reach1 + max_reach2)

start_star = find_star(source)
end_star = find_star(dest)

if not start_star or not end_star or not stars:
    print("Impossible")
elif start_star == end_star:
    print(1)
else:
    queue = deque([(start_star, 1)])
    visited = {start_star}
    found = False
    
    while queue:
        curr, dist = queue.popleft()
        for other in stars:
            if other not in visited and can_connect(curr, other):
                if other == end_star:
                    print(dist + 1)
                    found = True
                    break
                visited.add(other)
                queue.append((other, dist + 1))
        if found:
            break
    
    if not found:
        print("Impossible")
