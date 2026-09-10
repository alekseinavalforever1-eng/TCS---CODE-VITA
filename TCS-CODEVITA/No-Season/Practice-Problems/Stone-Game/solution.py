# Problem: Stone Game (Nim-Sum Game Theory)
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    K = int(input_data[1])
    piles = [int(x) for x in input_data[2:2+N]]
    
    # Grundy value for pile of size x when max move is K: x % (K + 1)
    nim_sum = 0
    for p in piles:
        nim_sum ^= (p % (K + 1))
        
    print("Player 1" if nim_sum != 0 else "Player 2")

if __name__ == "__main__":
    solve()
