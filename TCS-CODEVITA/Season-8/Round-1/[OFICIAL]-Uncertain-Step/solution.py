# Problem: Uncertain Steps
# Algorithm: Dynamic Programming (Ways to climb N stairs with 1, 2 or uncertain K step)
# Time Complexity: O(N)
# Space Complexity: O(N)

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    # dp[i][0]: ways without using the uncertain step (steps of 1 or 2)
    # dp[i][1]: ways having used exactly one uncertain step of size 3
    MOD = 1000000007
    if N <= 0:
        print(1)
        return
    dp = [[0, 0] for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        # Step 1
        dp[i][0] = (dp[i][0] + dp[i-1][0]) % MOD
        dp[i][1] = (dp[i][1] + dp[i-1][1]) % MOD
        # Step 2
        if i >= 2:
            dp[i][0] = (dp[i][0] + dp[i-2][0]) % MOD
            dp[i][1] = (dp[i][1] + dp[i-2][1]) % MOD
        # Uncertain step of size 3
        if i >= 3:
            dp[i][1] = (dp[i][1] + dp[i-3][0]) % MOD
            
    print((dp[N][0] + dp[N][1]) % MOD)

if __name__ == "__main__":
    solve()
