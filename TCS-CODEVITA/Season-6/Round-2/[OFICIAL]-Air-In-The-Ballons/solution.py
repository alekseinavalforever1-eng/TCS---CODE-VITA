# Problem: Air in the Balloons
# Algorithm: Greedy altitude & pressure equalization
# Time Complexity: O(N log N)
# Space Complexity: O(N)

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    balloons = [int(x) for x in input_data[1:1+N]]
    balloons.sort()
    avg = sum(balloons) / N
    moves = sum(abs(b - avg) for b in balloons) / 2
    print(int(moves))

if __name__ == "__main__":
    solve()
