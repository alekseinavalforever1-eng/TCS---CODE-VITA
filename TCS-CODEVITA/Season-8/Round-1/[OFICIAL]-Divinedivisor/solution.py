# Problem: Divine Divisors (Find all divisors of N)
# Algorithm: Sqrt Factorization
# Time Complexity: O(sqrt(N))
# Space Complexity: O(number of divisors)

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                divs.append(n // i)
    divs.sort()
    print(" ".join(map(str, divs)))

if __name__ == "__main__":
    solve()
