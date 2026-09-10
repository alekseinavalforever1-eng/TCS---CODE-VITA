def solve():
    target = input().strip()
    n = int(input().strip())
    pieces = input().strip().split()
    costs = list(map(int, input().strip().split()))
    
    target_len = len(target)
    
    def min_cost_without_rearrangement():
        # dp[i] = minimum cost to match target[0:i]
        dp = [float('inf')] * (target_len + 1)
        dp[0] = 0
        
        for i in range(target_len + 1):
            if dp[i] == float('inf'):
                continue
                
            for piece_idx, piece in enumerate(pieces):
                cost = costs[piece_idx]
                
                # Find how many characters we can match from target[i:]
                target_pos = i
                for char in piece:
                    if target_pos < target_len and char == target[target_pos]:
                        target_pos += 1
                
                if target_pos > i:
                    dp[target_pos] = min(dp[target_pos], dp[i] + cost)
        
        return dp[target_len]
    
    def min_cost_with_rearrangement():
        # When rearrangement is allowed, we can use characters in any order
        # dp[i] = minimum cost to match target[0:i]
        dp = [float('inf')] * (target_len + 1)
        dp[0] = 0
        
        for i in range(target_len + 1):
            if dp[i] == float('inf'):
                continue
                
            for piece_idx, piece in enumerate(pieces):
                cost = costs[piece_idx]
                
                # Count available characters in this piece
                piece_chars = {}
                for char in piece:
                    piece_chars[char] = piece_chars.get(char, 0) + 1
                
                # Try to match as many characters as possible from target[i:]
                target_pos = i
                while target_pos < target_len:
                    needed_char = target[target_pos]
                    if needed_char in piece_chars and piece_chars[needed_char] > 0:
                        piece_chars[needed_char] -= 1
                        target_pos += 1
                    else:
                        break
                
                if target_pos > i:
                    dp[target_pos] = min(dp[target_pos], dp[i] + cost)
        
        return dp[target_len]
    
    cost_without = min_cost_without_rearrangement()
    cost_with = min_cost_with_rearrangement()
    
    if cost_without == float('inf') or cost_with == float('inf'):
        print(-1)
    else:
        print(cost_without - cost_with)

solve()
