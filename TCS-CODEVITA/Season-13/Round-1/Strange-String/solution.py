def solve():
    target = input().strip()
    n = int(input().strip())
    pieces = input().strip().split()
    costs = list(map(int, input().strip().split()))
    
    target_len = len(target)
    INF = float('inf')
    
    # Precompute for efficiency
    piece_data = []
    for i in range(n):
        piece = pieces[i]
        cost = costs[i]
        
        # For rearrangement case: character counts
        char_count = {}
        for c in piece:
            char_count[c] = char_count.get(c, 0) + 1
        
        piece_data.append((piece, cost, char_count))
    
    def min_cost_without_rearrangement():
        dp = [INF] * (target_len + 1)
        dp[0] = 0
        
        for i in range(target_len):
            if dp[i] == INF:
                continue
                
            for piece, cost, _ in piece_data:
                target_pos = i
                for char in piece:
                    if target_pos < target_len and char == target[target_pos]:
                        target_pos += 1
                
                if target_pos > i:
                    dp[target_pos] = min(dp[target_pos], dp[i] + cost)
        
        return dp[target_len]
    
    def min_cost_with_rearrangement():
        dp = [INF] * (target_len + 1)
        dp[0] = 0
        
        for i in range(target_len):
            if dp[i] == INF:
                continue
                
            for piece, cost, char_count in piece_data:
                # Make a copy of available characters
                available = char_count.copy()
                
                target_pos = i
                while target_pos < target_len:
                    needed = target[target_pos]
                    if available.get(needed, 0) > 0:
                        available[needed] -= 1
                        target_pos += 1
                    else:
                        break
                
                if target_pos > i:
                    dp[target_pos] = min(dp[target_pos], dp[i] + cost)
        
        return dp[target_len]
    
    cost_without = min_cost_without_rearrangement()
    cost_with = min_cost_with_rearrangement()
    
    print(cost_without - cost_with)

solve()
