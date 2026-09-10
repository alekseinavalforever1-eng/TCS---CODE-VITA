# Problem: Largest Integer (Custom Comparator Sorting)
import sys
from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    nums = input_data[1:1+N]
    nums.sort(key=cmp_to_key(compare))
    ans = "".join(nums).lstrip("0")
    print(ans if ans else "0")

if __name__ == "__main__":
    solve()
