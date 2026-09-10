# Problem: Salary Paid (Employee Salary Calculation with Deductions)
# Algorithm: Simulation & Arithmetic
# Time Complexity: O(1)
# Space Complexity: O(1)

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    base = float(input_data[0])
    allowance = float(input_data[1])
    deduction = float(input_data[2])
    net = base + allowance - deduction
    print(f"{net:.2f}")

if __name__ == "__main__":
    solve()
