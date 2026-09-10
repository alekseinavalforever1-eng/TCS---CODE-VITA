def solve():
    time = input().strip()
    h, m = map(int, time.split(":"))
    Q = int(input().strip())
    A, B, X, Y = map(int, input().split())
    queries = [int(input().strip()) for _ in range(Q)]

    h_angle = (h % 12) * 30
    m_angle = m * 6

    def cost_to_form(target):
        current = abs(h_angle - m_angle)
        current = min(current, 360 - current)
        if current == target:
            return 0
        diff = abs(current - target)
        c1 = diff * Y * A
        c2 = diff * Y * B
        c3 = diff * X * A
        c4 = diff * X * B
        return min(c1, c2, c3, c4)

    total = sum(cost_to_form(q) for q in queries)
    print(total)

solve()
