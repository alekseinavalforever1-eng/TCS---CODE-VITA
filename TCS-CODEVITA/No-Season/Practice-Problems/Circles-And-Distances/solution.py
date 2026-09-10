# Problem: Circles and Distances (2D Geometry)
import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    x1, y1, r1 = map(float, input_data[:3])
    x2, y2, r2 = map(float, input_data[3:6])
    
    d = math.hypot(x2 - x1, y2 - y1)
    if d > r1 + r2:
        dist = d - (r1 + r2)
        print(f"Disjoint: {dist:.2f}")
    elif d < abs(r1 - r2):
        dist = abs(r1 - r2) - d
        print(f"Contained: {dist:.2f}")
    else:
        print("Intersecting: 0.00")

if __name__ == "__main__":
    solve()
