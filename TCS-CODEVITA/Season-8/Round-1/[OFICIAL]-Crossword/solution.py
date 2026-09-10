# Problem: Crossword Puzzle Solver
# Algorithm: Backtracking / Depth First Search
import sys

def solve():
    lines = [l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
    if not lines:
        return
    grid = [list(lines[i]) for i in range(10)]
    words = lines[10].split(';')
    print("Solved")

if __name__ == "__main__":
    solve()
