# Problem: Codekart (Shopping Cart Simulation)
import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    inventory = {}
    cart = {}
    total = 0.0
    for l in lines:
        parts = l.strip().split()
        if not parts:
            continue
        op = parts[0].upper()
        if op == "ADD":
            item, price, qty = parts[1], float(parts[2]), int(parts[3])
            inventory[item] = price
            cart[item] = cart.get(item, 0) + qty
        elif op == "REMOVE":
            item = parts[1]
            cart.pop(item, None)
        elif op == "CHECKOUT":
            for item, qty in cart.items():
                total += inventory.get(item, 0) * qty
            print(f"{total:.2f}")
            return

if __name__ == "__main__":
    solve()
