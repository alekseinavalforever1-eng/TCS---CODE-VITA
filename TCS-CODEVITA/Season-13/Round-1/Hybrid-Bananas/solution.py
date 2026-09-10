from collections import defaultdict, deque

# Read input
N = int(input())
lines = []
for _ in range(N):
    lines.append(input().strip())

# Last line: source and destination
source, dest = map(int, lines[-1].split())
lines = lines[:-1]  # remove last line

graph = defaultdict(list)
tree_lines = []

# Parse trees
for line in lines:
    if line == 'break':
        # Process current tree
        for l in tree_lines:
            nums = list(map(int, l.split()))
            if len(nums) >= 2:
                parent = nums[0]
                for child in nums[1:]:
                    # Down: parent -> child (0 cost), Up: child -> parent (1 cost)
                    graph[parent].append((child, 0))  # down
                    graph[child].append((parent, 1))  # up
        tree_lines = []
    else:
        tree_lines.append(line)

# Process remaining lines if any
for l in tree_lines:
    nums = list(map(int, l.split()))
    if len(nums) >= 2:
        parent = nums[0]
        for child in nums[1:]:
            graph[parent].append((child, 0))
            graph[child].append((parent, 1))

# 0-1 BFS
from collections import deque

dist = defaultdict(lambda: float('inf'))
dist[source] = 0
dq = deque()
dq.append(source)

while dq:
    node = dq.popleft()
    for neighbor, cost in graph[node]:
        if dist[node] + cost < dist[neighbor]:
            dist[neighbor] = dist[node] + cost
            if cost == 0:
                dq.appendleft(neighbor)
            else:
                dq.append(neighbor)

print(dist[dest])
