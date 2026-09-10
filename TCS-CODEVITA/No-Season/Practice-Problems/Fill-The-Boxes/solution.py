# Problem: Fill The Boxes (Bin Packing / Greedy)
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    N = int(next(it))
    items = sorted([int(next(it)) for _ in range(N)], reverse=True)
    M = int(next(it))
    boxes = sorted([int(next(it)) for _ in range(M)], reverse=True)
    
    # Best-fit decreasing heuristic
    box_rem = list(boxes)
    used = 0
    for item in items:
        # Find tightest box that can fit item
        best_idx = -1
        min_space_left = float('inf')
        for i in range(len(box_rem)):
            if box_rem[i] >= item and (box_rem[i] - item) < min_space_left:
                min_space_left = box_rem[i] - item
                best_idx = i
        if best_idx == -1:
            print(-1)
            return
        box_rem[best_idx] -= item
        
    used = sum(1 for i in range(len(boxes)) if box_rem[i] < boxes[i])
    print(used)

if __name__ == "__main__":
    solve()
