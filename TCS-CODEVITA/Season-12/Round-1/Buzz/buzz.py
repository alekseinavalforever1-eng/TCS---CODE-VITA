def bds(n, ids, costs, a):
    free = {}
    
    # Map item IDs to their costs
    id_cost = {ids[i]: costs[i] for i in range(n)}
    
    # Calculate free items based on factors
    for i in range(n):
        k = ids[i]
        if id_cost[k] <= a:  # Only consider if we can buy this item
            cnt = a // id_cost[k]  # How many we can buy
            for j in range(1, k + 1):
                if k % j == 0 and j in id_cost:  # Check factors
                    if j not in free:
                        free[j] = 0
                    free[j] += cnt
    
    # Determine max free items and worth
    max_cnt = 0
    max_worth = 0
    
    for fid, cnt in free.items():
        worth = cnt * id_cost[fid]
        if cnt > max_cnt or (cnt == max_cnt and worth > max_worth):
            max_cnt = cnt
            max_worth = worth
            
    return max_cnt, max_worth

# Input reading and function execution
n = int(input())
ids = list(map(int, input().split()))
costs = list(map(int, input().split()))
a = int(input())

res = bds(n, ids, costs, a)
print(res[0], res[1])
