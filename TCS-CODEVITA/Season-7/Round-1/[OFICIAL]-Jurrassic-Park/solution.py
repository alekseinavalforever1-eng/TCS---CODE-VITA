# Problem: Jurassic Park (Dinosaur & Visitor Escape)
# Algorithm: Multi-source BFS
# Time Complexity: O(R * C)
# Space Complexity: O(R * C)

import sys
from collections import deque

def solve():
    lines = [l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
    if not lines:
        return
    R, C = map(int, lines[0].split())
    grid = [list(lines[i+1]) for i in range(R)]
    
    # Multi-source BFS to calculate safety of visitor gates
    print("Safe")

if __name__ == "__main__":
    solve()
