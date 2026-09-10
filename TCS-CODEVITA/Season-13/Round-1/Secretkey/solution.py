def solve():
    import sys
    sys.setrecursionlimit(10000)
    
    N, M = map(int, input().split())
    grid = [input().split() for _ in range(N)]
    
    T = int(input().strip())
    I = int(input().strip())

    # Each time t -> valid positions (start all True)
    valid = [[[True for _ in range(M)] for _ in range(N)] for _ in range(T+1)]

    for _ in range(I):
        t = int(input().strip())
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1-1, x2):
            for j in range(y1-1, y2):
                if 0 <= i < N and 0 <= j < M:
                    valid[t][i][j] = False

    # If any time step fully invalid -> not enough clues
    for t in range(1, T+1):
        if not any(valid[t][i][j] for i in range(N) for j in range(M)):
            print("Not enough clues", end="")
            return

    # Get all valid cells for each time
    positions = [[] for _ in range(T+1)]
    for t in range(1, T+1):
        for i in range(N):
            for j in range(M):
                if valid[t][i][j]:
                    positions[t].append((i, j))

    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    paths = []
    visited = [[False]*M for _ in range(N)]

    def dfs(t, i, j, path):
        if not valid[t][i][j]:
            return
        if visited[i][j]:
            return
        if t == T:
            paths.append(path + [(i, j)])
            if len(paths) > 1:
                return
            return

        visited[i][j] = True
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < M and valid[t+1][ni][nj]:
                dfs(t+1, ni, nj, path + [(i, j)])
                if len(paths) > 1:
                    return
        visited[i][j] = False

    # Try all valid starting cells for t=1
    for i, j in positions[1]:
        dfs(1, i, j, [])
        if len(paths) > 1:
            break

    if len(paths) == 1:
        path = paths[0]
        word = ''.join(grid[x][y] for x, y in path)
        print(word, end="")
    else:
        print("Not enough clues", end="")

if __name__ == "__main__":
    solve()
