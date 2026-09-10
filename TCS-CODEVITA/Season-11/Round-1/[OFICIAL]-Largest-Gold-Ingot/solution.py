# Problem: Largest Gold Ingot (Largest Rectangle in Histogram)
# Algorithm: Monotonic Stack
# Time Complexity: O(N)
# Space Complexity: O(N)

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    # Length of gold bar and number of heights
    B = int(input_data[0])
    N = int(input_data[1])
    heights = [int(x) for x in input_data[2:2+N]]
    
    stack = []
    max_area = 0
    
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            prev_idx, prev_h = stack.pop()
            width = i - prev_idx
            max_area = max(max_area, width * prev_h)
            start = prev_idx
        stack.append((start, h))
        
    for idx, h in stack:
        width = N - idx
        max_area = max(max_area, width * h)
        
    # Maximum volume/value of ingot is max_area * B mod 10^9 + 7 if required, or directly max_area * B
    print(max_area * B)

if __name__ == "__main__":
    solve()
