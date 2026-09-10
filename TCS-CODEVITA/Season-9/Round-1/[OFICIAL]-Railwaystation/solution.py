# Problem: Railway Station (Minimum Platforms Needed)
# Algorithm: Event Sorting / Interval Sweep-line
# Time Complexity: O(N log N)
# Space Complexity: O(N)

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arrivals = []
    departures = []
    idx = 1
    for _ in range(n):
        arr = int(input_data[idx])
        dur = int(input_data[idx+1])
        idx += 2
        arrivals.append(arr)
        departures.append(arr + dur)
        
    arrivals.sort()
    departures.sort()
    
    platforms_needed = 0
    max_platforms = 0
    i, j = 0, 0
    
    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:
            platforms_needed -= 1
            j += 1
            
    print(max_platforms)

if __name__ == "__main__":
    solve()
