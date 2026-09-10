# Problem: RLE String (Run-Length Encoding)
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    if not s:
        print("")
        return
    res = []
    i = 0
    while i < len(s):
        char = s[i]
        count = 1
        while i + 1 < len(s) and s[i+1] == char:
            count += 1
            i += 1
        res.append(f"{char}{count}")
        i += 1
    print("".join(res))

if __name__ == "__main__":
    solve()
