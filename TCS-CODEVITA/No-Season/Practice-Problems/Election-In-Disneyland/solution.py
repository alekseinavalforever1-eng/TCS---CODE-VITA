# Problem: Election in Disneyland (Boyer-Moore Majority Vote)
import sys
from collections import Counter

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    votes = input_data[1:1+N]
    counts = Counter(votes)
    winner, max_v = counts.most_common(1)[0]
    if max_v > N / 2:
        print(winner)
    else:
        print("Runoff required")

if __name__ == "__main__":
    solve()
