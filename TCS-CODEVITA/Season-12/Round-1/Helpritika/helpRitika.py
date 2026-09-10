def can_form_main_string(n, substrings, main_str, k):
    m = len(main_str)
    dp = [[float('inf')] * (k + 1) for _ in range(m + 1)]
    dp[0][0] = 0  # No characters formed with 0 deletions

    for i in range(m):
        for j in range(k + 1):
            if dp[i][j] == float('inf'):
                continue
            for sub in substrings:
                
                delete_count = sum(1 for char in sub if char not in main_str[i:])
                if j + delete_count <= k:
                    # Try to match the substring to the main string
                    match_length = sum(1 for char in sub if char == main_str[i + sum(1 for char in sub if char in main_str[i:])])
                    if i + match_length <= m:
                        dp[i + match_length][j + delete_count] = min(dp[i + match_length][j + delete_count], dp[i][j])

   
    min_deletions_needed = min(dp[m])
    
    if min_deletions_needed == float('inf'):
        return "Impossible"
    
    if min_deletions_needed <= k:
        return "Possible"
  
    max_length = 0
    for j in range(k + 1):
        if dp[m][j] <= k:
            max_length = m

    return main_str[:max_length]


n = int(input())
substrings = [input().strip() for _ in range(n)]
main_str = input().strip()
k = int(input())

result = can_form_main_string(n, substrings, main_str, k)
print(result)
