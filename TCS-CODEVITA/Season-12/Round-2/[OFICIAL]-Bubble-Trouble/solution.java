import math
from collections import deque

def circles_overlap(x1, y1, r1, x2, y2, r2):
    """Check if two circles overlap (distance < sum of radii)."""
    dist = math.hypot(x1 - x2, y1 - y2)
    return dist < (r1 + r2)

def crosses_tax_line(p1, p2, b1, b2):
    """Check if segment p1-p2 crosses building centre line b1-b2."""
    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
    return (ccw(p1, b1, b2) != ccw(p2, b1, b2)) and (ccw(p1, p2, b1) != ccw(p1, p2, b2))

def bfs(start, end, buildings, tax_lines, S, vehicle_r):
    """BFS to find minimum tax lines crossed."""
    visited = set()
    queue = deque()
    queue.append((start[0], start[1], 0))  # (x, y, tax_count)

    while queue:
        x, y, tax_count = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Check if reached destination
        if math.isclose(x, end[0], abs_tol=0.5) and math.isclose(y, end[1], abs_tol=0.5):
            return tax_count

        # Try 4 directions
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy

            if not (0 <= nx <= S and 0 <= ny <= S):
                continue

            # Check building collision
            if any(circles_overlap(nx, ny, vehicle_r, bx, by, br) for bx, by, br in buildings):
                continue

            # Count tax line crossing
            add_tax = 0
            for i1, i2 in tax_lines:
                b1 = buildings[i1]
                b2 = buildings[i2]
                if crosses_tax_line((x,y), (nx,ny), (b1[0], b1[1]), (b2[0], b2[1])):
                    add_tax += 1

            queue.append((nx, ny, tax_count + add_tax))

    return None  # unreachable

# Read input
S = int(input().strip())
sx, sy, sr = map(int, input().split())
dx, dy = map(int, input().split())
N = int(input().strip())
buildings = []
for _ in range(N):
    bx, by, br = map(int, input().split())
    buildings.append((bx, by, br))

T = int(input().strip())
tax_lines = []
for _ in range(T):
    a, b = map(int, input().split())
    tax_lines.append((a-1, b-1))  # convert to 0-index

# Check start/destination collision
if any(circles_overlap(sx, sy, sr, bx, by, br) for bx, by, br in buildings) or \
   any(circles_overlap(dx, dy, sr, bx, by, br) for bx, by, br in buildings):
    print("Impossible")
else:
    result = bfs((sx, sy), (dx, dy), buildings, tax_lines, S, sr)
    print(result if result is not None else "Impossible")
