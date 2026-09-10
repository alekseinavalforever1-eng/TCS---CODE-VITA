# Problem: Counting Rectangles
# Algorithm: Point Pair Diagonal Hash Check
# Time Complexity: O(N^2)
# Space Complexity: O(N)

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    points = set()
    pts = []
    idx = 1
    for _ in range(n):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        idx += 2
        points.add((x, y))
        pts.append((x, y))
        
    rect_count = 0
    # For axis-aligned rectangles:
    for i in range(n):
        x1, y1 = pts[i]
        for j in range(i + 1, n):
            x2, y2 = pts[j]
            # Must be diagonal points with different x and y
            if x1 != x2 and y1 != y2:
                if (x1, y2) in points and (x2, y1) in points:
                    rect_count += 1
                    
    # Each rectangle counted twice (two diagonals)
    print(rect_count // 2)

if __name__ == "__main__":
    solve()
