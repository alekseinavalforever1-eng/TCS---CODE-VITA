import heapq

# Dice roll updates
def roll_dice(top, left, front, direction):
    if direction == 'right':
        return 7-left, top, front
    if direction == 'left':
        return left, 7-top, front
    if direction == 'up':
        return front, left, 7-top
    if direction == 'down':
        return 7-front, left, top
    return top, left, front

# Read input
N = int(input())
placements = [input().split() for _ in range(N)]
placements = [(int(a), int(b), c) for a,b,c in placements]
placements.sort()  # sort by first cube then second cube

# Build cube coordinates
cube_pos = dict()
cube_pos[placements[0][0]] = (0,0)  # arbitrary origin
for a,b,d in placements:
    if a not in cube_pos:
        continue
    x,y = cube_pos[a]
    if d == 'left':
        new_pos = (x-1, y)
    elif d == 'right':
        new_pos = (x+1, y)
    elif d == 'up':
        new_pos = (x, y+1)
    elif d == 'down':
        new_pos = (x, y-1)
    # remove overlap if exists
    for k,v in list(cube_pos.items()):
        if v == new_pos:
            del cube_pos[k]
    cube_pos[b] = new_pos

source, dest = map(int, input().split())
top, left, front = map(int, input().split())

# Build adjacency mapping
coord_to_cube = {v:k for k,v in cube_pos.items()}
moves = [(0,1,'up'),(0,-1,'down'),(1,0,'right'),(-1,0,'left')]

# Dijkstra
pq = []
heapq.heappush(pq, (0, source, (top, left, front)))
visited = dict()  # (cube_id, dice_orientation) -> min_cost

while pq:
    cost, cube, orient = heapq.heappop(pq)
    if (cube, orient) in visited:
        continue
    visited[(cube, orient)] = cost
    if cube == dest:
        print(cost)
        break
    x,y = cube_pos[cube]
    for dx,dy,dir in moves:
        nx,ny = x+dx, y+dy
        if (nx,ny) in coord_to_cube:
            next_cube = coord_to_cube[(nx,ny)]
            new_orient = roll_dice(*orient, dir)
            new_cost = cost + new_orient[0]  # top face
            if (next_cube,new_orient) not in visited:
                heapq.heappush(pq,(new_cost,next_cube,new_orient))
else:
    print("Impossible")
