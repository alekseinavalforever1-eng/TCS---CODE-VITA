# Problem: Prime Faces (Dice Combinations)
# Algorithm: Dynamic Programming / Combinatorics
# Time Complexity: O(N)
# Space Complexity: O(N)

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    # Dice faces that are prime: {2, 3, 5}
    # Number of dice D, target sum S
    D = int(input_data[0])
    S = int(input_data[1])
    
    primes = [2, 3, 5]
    dp = [0] * (S + 1)
    dp[0] = 1
    
    for _ in range(D):
        new_dp = [0] * (S + 1)
        for s in range(S + 1):
            if dp[s] > 0:
                for p in primes:
                    if s + p <= S:
                        new_dp[s + p] += dp[s]
        dp = new_dp
        
    print(dp[S])

if __name__ == "__main__":
    solve()
