# Problem: Lazy Student (Probability of knowing at least one test question)
# Algorithm: Combinatorics & Modular Inverse
# Time Complexity: O(N)
# Space Complexity: O(1)

import sys
import math

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return math.comb(n, r)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    idx = 1
    for _ in range(T):
        total_q = int(input_data[idx])
        test_q = int(input_data[idx+1])
        prepared_q = int(input_data[idx+2])
        idx += 3
        
        # Total ways to choose test questions: comb(total_q, test_q)
        # Ways to choose none from prepared questions: comb(total_q - prepared_q, test_q)
        total_ways = nCr(total_q, test_q)
        unprepared_q = total_q - prepared_q
        unfavorable = nCr(unprepared_q, test_q)
        favorable = total_ways - unfavorable
        
        # Output as fraction or modular inverse
        g = math.gcd(favorable, total_ways)
        p = favorable // g
        q = total_ways // g
        print(f"{p}/{q}")

if __name__ == "__main__":
    solve()
