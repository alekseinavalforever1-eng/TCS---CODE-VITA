# Problem: Prime Time Again
# Algorithm: Math & Sieve of Eratosthenes
# Time Complexity: O(D log log D)
# Space Complexity: O(D)

import sys

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return is_prime

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    D = int(input_data[0])
    P = int(input_data[1])
    
    if D % P != 0:
        print(0)
        return
        
    part_len = D // P
    is_prime = sieve(D)
    
    # Check each hour slot in the first part [1..part_len]
    # For a slot to be valid, corresponding hour in EVERY part must be prime
    valid_groups = 0
    for h in range(2, part_len + 1):
        all_prime = True
        for part in range(P):
            val = h + part * part_len
            if val > D or not is_prime[val]:
                all_prime = False
                break
        if all_prime:
            valid_groups += 1
            
    print(valid_groups)

if __name__ == "__main__":
    solve()
