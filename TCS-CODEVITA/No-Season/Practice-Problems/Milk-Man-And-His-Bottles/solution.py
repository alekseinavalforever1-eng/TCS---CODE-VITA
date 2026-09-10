# Problem: Milk Man and his Bottles (Coin Change DP)
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    queries = [int(x) for x in input_data[1:1+T]]
    if not queries:
        return
    max_L = max(queries)
    bottles = [1, 5, 7, 10]
    dp = [float('inf')] * (max_L + 1)
    dp[0] = 0
    for b in bottles:
        for i in range(b, max_L + 1):
            if dp[i - b] + 1 < dp[i]:
                dp[i] = dp[i - b] + 1
    for q in queries:
        print(dp[q])

if __name__ == "__main__":
    solve()
