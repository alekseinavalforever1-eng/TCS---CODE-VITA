import math

def distance(p1, p2):
    """Straight line distance in 3D."""
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

def same_face(p1, p2):
    """Check if two points are on the same face of the cube."""
    # Same z (top or side), or same x or y on side faces
    return (p1[2] == p2[2]) or (p1[0] == p2[0]) or (p1[1] == p2[1])

def surface_distance(p1, p2):
    """Shortest path along surface of cube (not bottom)."""
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    L = 10  # cube side

    # Possible unfoldings (avoid z=0 side)
    candidates = []

    # If both on top (z=10) or sides:
    # Try flattening each adjacent pair of faces
    if z1 == 10 and z2 == 10:
        # Both on top face, direct straight line
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    # Try different face unfoldings
    # Each unfolding gives a possible 2D distance
    # We consider only valid paths (z != 0)
    if z1 != 0 and z2 != 0:
        # Faces parallel to x=0, x=10
        candidates.append(math.sqrt((abs(x1 - x2) + abs(z1 - z2))**2 + (y1 - y2)**2))
        # Faces parallel to y=0, y=10
        candidates.append(math.sqrt((abs(y1 - y2) + abs(z1 - z2))**2 + (x1 - x2)**2))
        # Faces parallel to z=10 (top)
        candidates.append(math.sqrt((abs(z1 - z2) + abs(x1 - x2))**2 + (y1 - y2)**2))

    return min(candidates)

def beetle_path(points):
    total = 0.0
    for i in range(len(points)-1):
        p1, p2 = points[i], points[i+1]
        if same_face(p1, p2):
            r = distance(p1, p2)
            d = (math.pi * r) / 3  # arc distance (60 degrees)
        else:
            d = surface_distance(p1, p2)
        total += round(d, 2)
    return round(total, 2)

# Example input
if __name__ == "__main__":
    n = int(input("Enter number of honey spots: "))
    points = []
    print("Enter coordinates (x y z) for beetle start and honey spots:")
    for _ in range(n+1):  # including starting point
        x, y, z = map(float, input().split())
        points.append((x, y, z))
    
    print("Total distance travelled:", beetle_path(points))
