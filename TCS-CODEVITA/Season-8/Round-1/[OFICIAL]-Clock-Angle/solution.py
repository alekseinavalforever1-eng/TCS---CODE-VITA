# Problem: Clock Angle
# Algorithm: Angle formula |30*H - 5.5*M|
# Time Complexity: O(1)
# Space Complexity: O(1)

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    H = int(input_data[0])
    M = float(input_data[1]) if len(input_data) > 1 else 0.0
    
    h_angle = (H % 12) * 30 + M * 0.5
    m_angle = M * 6
    diff = abs(h_angle - m_angle)
    angle = min(diff, 360 - diff)
    print(f"{angle:.2f}")

if __name__ == "__main__":
    solve()
