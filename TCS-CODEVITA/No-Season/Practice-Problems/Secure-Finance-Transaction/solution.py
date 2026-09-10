# Problem: Secure Finance Transaction (Modular Arithmetic)
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    S = int(input_data[0])
    D = int(input_data[1])
    N = int(input_data[2])
    C = int(input_data[3])
    
    val = pow(S, D, N)
    print("VALID" if val == C else "INVALID")

if __name__ == "__main__":
    solve()
