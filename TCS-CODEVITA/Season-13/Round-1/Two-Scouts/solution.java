from collections import deque, defaultdict

def solve():
    try:
        n, m = map(int, input().split())
        g = defaultdict(list)

        for _ in range(m):
            a, b = map(int, input().split())
            g[a].append(b)
            g[b].append(a)

        a1, a2 = map(int, input().split())
        t = int(input())

        if a1 == a2:
            print(0 if a1 == t else "Impossible")
            return

        if a1 == t and a2 == t:
            print(0)
            return

        def bfs(s, e):
            if s == e:
                return True
            q = deque([s])
            vis = {s}
            while q:
                u = q.popleft()
                if u == e:
                    return True
                for v in g[u]:
                    if v not in vis:
                        vis.add(v)
                        q.append(v)
            return False

        if not bfs(a1, t) or not bfs(a2, t):
            print("Impossible")
            return

        st = (a1, a2, 1 << a1, 1 << a2)
        q = deque([st])
        vis = {st}
        ans = float('inf')

        while q:
            x1, x2, m1, m2 = q.popleft()
            cmb = m1 | m2
            cnt = bin(cmb).count("1")

            if cnt >= ans:
                continue

            if x1 == t and x2 == t:
                ans = min(ans, cnt - 1)
                continue

            nxt1 = [x1] if x1 == t else g[x1]
            nxt2 = [x2] if x2 == t else g[x2]

            for y1 in nxt1:
                if y1 != t and (m1 >> y1) & 1:
                    continue
                for y2 in nxt2:
                    if y2 != t and (m2 >> y2) & 1:
                        continue
                    if y1 != t and (m2 >> y1) & 1:
                        continue
                    if y2 != t and (m1 >> y2) & 1:
                        continue
                    if y1 == y2 and y1 != t:
                        continue

                    nm1 = m1 | (1 << y1)
                    nm2 = m2 | (1 << y2)
                    ncnt = bin(nm1 | nm2).count("1")

                    if ncnt >= ans:
                        continue

                    ns = (y1, y2, nm1, nm2)
                    if ns not in vis:
                        vis.add(ns)
                        q.append(ns)

        print(ans if ans < float('inf') else "Impossible")

    except Exception:
        print("Impossible")

solve()
