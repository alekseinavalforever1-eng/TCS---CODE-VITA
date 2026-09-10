# Problem: Hedger (Portfolio Profit Maximization)
# Algorithm: Greedy / Fractional Knapsack
# Time Complexity: O(N log N)
# Space Complexity: O(N)

import sys

def solve():
    lines = [l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
    if not lines:
        return
    # Input format:
    # N (number of assets), K (budget)
    # prices of assets
    # profits / expected returns
    tokens = []
    for l in lines:
        tokens.extend(l.split())
    if not tokens:
        return
    N = int(tokens[0])
    K = float(tokens[1])
    prices = [float(x) for x in tokens[2:2+N]]
    profits = [float(x) for x in tokens[2+N:2+2*N]]
    
    # ratio of profit / price
    items = []
    for i in range(N):
        if prices[i] > 0:
            items.append((profits[i] / prices[i], prices[i], profits[i]))
            
    items.sort(key=lambda x: x[0], reverse=True)
    
    total_profit = 0.0
    rem_budget = K
    
    for ratio, price, profit in items:
        if rem_budget <= 0:
            break
        take = min(rem_budget, price)
        total_profit += (take / price) * profit
        rem_budget -= take
        
    print(int(round(total_profit)))

if __name__ == "__main__":
    solve()
