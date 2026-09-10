# Problem: Minimum Office Hours (Employee badge sweep & intervals)
# Algorithm: Sweep-line / Disjoint Interval Union
# Time Complexity: O(N log N)
# Space Complexity: O(N)

import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    # Read target hours and swipe log intervals
    # Format: mandatory hours M, then swipe pairs (entry, exit)
    lines = [l.strip() for l in input_data if l.strip()]
    if not lines:
        return
    
    M = int(lines[0].split()[0])
    intervals = []
    for l in lines[1:]:
        parts = l.split()
        if len(parts) >= 2:
            t1 = int(parts[0].replace(":", ""))
            t2 = int(parts[1].replace(":", ""))
            intervals.append((t1, t2))
            
    intervals.sort()
    # Merge overlapping intervals
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
            
    total_minutes = sum(end - start for start, end in merged)
    print("Compliant" if total_minutes >= M * 60 else f"Short by {M*60 - total_minutes}")

if __name__ == "__main__":
    solve()
