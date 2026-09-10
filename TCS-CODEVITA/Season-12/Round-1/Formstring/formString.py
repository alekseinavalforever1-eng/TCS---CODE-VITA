import time

def max_alt_worth(b_str, w):
    n = len(b_str)
    
    # Calculate total worth of the string
    total_w = sum(w)
    
    # To find the maximum worth of the alternating string
    max_w = 0
    
    # Check for both patterns: starting with '0' and '1'
    for s in (0, 1):
        curr_w = 0
        exp = s
        
        for i in range(n):
            if int(b_str[i]) == exp:
                curr_w += w[i]
                exp = 1 - exp  # Alternate between 0 and 1
        
        max_w = max(max_w, curr_w)

    # The worth of characters to be removed is total worth minus the max worth of the alternating string
    return total_w - max_w

# Input reading
b_str = input().strip()
w = list(map(int, input().strip().split()))

# Measure execution time
start_time = time.time()
result = max_alt_worth(b_str, w)
end_time = time.time()

# Output the result and execution time
print(result)
print(f"Execution Time: {end_time - start_time:.6f} seconds")
