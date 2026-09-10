# Problem: Work Life Balance (Task scheduling)
# Algorithm: Greedy Interval Scheduling
# Time Complexity: O(N log N)
# Space Complexity: O(N)

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    tasks = []
    idx = 1
    for _ in range(n):
        s = int(input_data[idx])
        e = int(input_data[idx+1])
        tasks.append((s, e))
        idx += 2
    tasks.sort(key=lambda x: x[1])
    count = 0
    last_end = -1
    for s, e in tasks:
        if s >= last_end:
            count += 1
            last_end = e
    print(count)

if __name__ == "__main__":
    solve()
