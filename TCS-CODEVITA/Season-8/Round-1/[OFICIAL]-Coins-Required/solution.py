# Problem: Coins Required (Greedy Coins 5, 2, 1)
# Algorithm: Greedy Mathematical Partition
# Time Complexity: O(1)
# Space Complexity: O(1)

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    # Must have at least one 1-rupee and one 2-rupee coin
    # Number of 5 rupee coins
    c5 = (n - 4) // 5
    rem = n - c5 * 5
    if rem % 2 == 0:
        c1 = 2
        c2 = (rem - 2) // 2
    else:
        c1 = 1
        c2 = (rem - 1) // 2
        
    print(f"{c5 + c2 + c1} {c5} {c2} {c1}")

if __name__ == "__main__":
    solve()
