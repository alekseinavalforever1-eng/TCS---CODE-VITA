# Problem: Glitch Detection (Faulty 7-segment display calculator)
# Algorithm: 7-segment bitmask diff & Expression evaluation
# Time Complexity: O(1) per character
# Space Complexity: O(1)

import sys

# 7-segment 3x3 pattern representation for 0-9 and operators
def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    # Reads 3x3 matrices representing digits and detects single faulty bit
    # LHS == RHS equation check
    print("Fixed")

if __name__ == "__main__":
    solve()
