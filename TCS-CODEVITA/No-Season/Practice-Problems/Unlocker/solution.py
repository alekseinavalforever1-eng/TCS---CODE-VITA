# Problem: Unlocker (Circular Distance Simulation)
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    curr = input_data[1]
    target = input_data[2]
    steps = 0
    for c, t in zip(curr, target):
        d1 = int(c)
        d2 = int(t)
        diff = abs(d1 - d2)
        steps += min(diff, 10 - diff)
    print(steps)

if __name__ == "__main__":
    solve()
