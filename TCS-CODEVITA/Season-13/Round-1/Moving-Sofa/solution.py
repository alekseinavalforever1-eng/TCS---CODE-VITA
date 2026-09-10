from collections import deque

def get_sofa_positions(matrix, char):
    """Finds the two cells occupied by 's' or 'S' and returns orientation and anchor position."""
    positions = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == char:
                positions.append((i, j))
    positions.sort()
    (x1, y1), (x2, y2) = positions
    if x1 == x2:  # Horizontal
        return (x1, min(y1, y2), "H")
    else:  # Vertical
        return (min(x1, x2), y1, "V")

def valid_move(x, y, orient, dx, dy, matrix):
    """Checks if sofa can move to new position."""
    M, N = len(matrix), len(matrix[0])
    nx, ny = x + dx, y + dy
    if orient == "H":
        if 0 <= nx < M and 0 <= ny < N-1:
            return matrix[nx][ny] != "H" and matrix[nx][ny+1] != "H"
    else:  # Vertical
        if 0 <= nx < M-1 and 0 <= ny < N:
            return matrix[nx][ny] != "H" and matrix[nx+1][ny] != "H"
    return False

def can_rotate(x, y, orient, matrix):
    """Checks if sofa can rotate inside 2x2 free block."""
    M, N = len(matrix), len(matrix[0])
    if x < 0 or y < 0 or x >= M-1 or y >= N-1:
        return False
    for i in range(x, x+2):
        for j in range(y, y+2):
            if matrix[i][j] == "H":
                return False
    return True

def bfs(matrix, start, target):
    M, N = len(matrix), len(matrix[0])
    queue = deque()
    visited = set()
    
    queue.append((start[0], start[1], start[2], 0))  # (x, y, orientation, steps)
    visited.add((start[0], start[1], start[2]))
    
    while queue:
        x, y, orient, steps = queue.popleft()
        
        if (x, y, orient) == target:
            return steps
        
        # Try moving in 4 directions
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            if valid_move(x, y, orient, dx, dy, matrix):
                nx, ny = x + dx, y + dy
                new_state = (nx, ny, orient)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((nx, ny, orient, steps+1))
        
        # Try rotating
        if can_rotate(x, y, orient, matrix):
            new_orient = "H" if orient == "V" else "V"
            new_state = (x, y, new_orient)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((x, y, new_orient, steps+1))
    
    return "Impossible"

# ----------------- MAIN -----------------
if __name__ == "__main__":
    M, N = map(int, input().split())
    matrix = [input().split() for _ in range(M)]
    
    start = get_sofa_positions(matrix, "s")
    target = get_sofa_positions(matrix, "S")
    
    ans = bfs(matrix, start, target)
    print(ans)
