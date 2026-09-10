import sys
sys.setrecursionlimit(10000)

def solve():
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        line = input().strip()
        tokens = line.split()
        if len(tokens) == M:
            grid.append(tokens)
        else:
            s = line.replace(' ', '')
            if len(s) == M:
                grid.append(list(s))
            else:
                grid.append(list(tokens[0]))
    sx, sy = map(int, input().split())
    pearl, platinum, gold, diamond = map(int, input().split())
    K = int(input().strip())
    val = {'$': pearl, '*': platinum, '%': gold, '+': diamond}
    
    def treasure_value(r, c):
        return val.get(grid[r][c], 0)
    
    def is_treasure_cell(r, c):
        return grid[r][c] in val
    
    def is_stable(r, c):
        if r == N - 1:
            return True
        return grid[r + 1][c] == '#'
    
    best = 0
    memo = {}
    
    def dfs(r, c, steps, collected, visited):
        nonlocal best
        vfs = frozenset(visited)
        key = (r, c, steps, vfs)
        prev = memo.get(key)
        if prev is not None and prev >= collected:
            return
        memo[key] = collected
        if (r, c) not in visited and is_treasure_cell(r, c):
            collected += treasure_value(r, c)
            visited = visited | {(r, c)}
        if is_stable(r, c) and r != N - 1:
            best = max(best, collected)
        if steps >= K:
            return
        # move left and right
        for dc in (-1, 1):
            nr, nc = r, c + dc
            if not (0 <= nc < M) or grid[nr][nc] == '#':
                continue
            steps_after = steps + 1
            cur_r, cur_c = nr, nc
            col = collected
            vis = visited
            if (cur_r, cur_c) not in vis and is_treasure_cell(cur_r, cur_c):
                col += treasure_value(cur_r, cur_c)
                vis = vis | {(cur_r, cur_c)}
            # slide down (gravity)
            while cur_r + 1 < N and grid[cur_r + 1][cur_c] != '#':
                cur_r += 1
                steps_after += 1
                if steps_after > K:
                    break
                if (cur_r, cur_c) not in vis and is_treasure_cell(cur_r, cur_c):
                    col += treasure_value(cur_r, cur_c)
                    vis = vis | {(cur_r, cur_c)}
            if steps_after <= K:
                dfs(cur_r, cur_c, steps_after, col, vis)
        # climb up
        if r - 2 >= 0 and grid[r - 1][c] == '#' and grid[r - 2][c] != '#':
            tr, tc = r - 2, c
            steps_after = steps + 1
            col = collected
            vis = visited
            if (tr, tc) not in vis and is_treasure_cell(tr, tc):
                col += treasure_value(tr, tc)
                vis = vis | {(tr, tc)}
            while tr + 1 < N and grid[tr + 1][tc] != '#':
                tr += 1
                steps_after += 1
                if steps_after > K:
                    break
                if (tr, tc) not in vis and is_treasure_cell(tr, tc):
                    col += treasure_value(tr, tc)
                    vis = vis | {(tr, tc)}
            if steps_after <= K:
                dfs(tr, tc, steps_after, col, vis)
    
    dfs(sx, sy, 0, 0, frozenset())
    sys.stdout.write(str(best))

if _name_ == "_main_":
    solve()
