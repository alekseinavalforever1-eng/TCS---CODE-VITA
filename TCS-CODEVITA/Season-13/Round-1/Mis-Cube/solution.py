"""
Mis Cube - Final Solution

Based on standard 2x2 cube layout where each face has 4 stickers numbered 0-3:
Face layout in input: Top, Front, Down, Back, Left, Right (24 stickers total)

Indices: 0-3 (Top), 4-7 (Front), 8-11 (Down), 12-15 (Back), 16-19 (Left), 20-23 (Right)
"""

def solve():
    colors = input().split()
    
    # All 8 corners with their 3 sticker positions
    # Trying different corner mappings based on standard cube notation
    corners = [
        (0, 4, 16),    # Top-Front-Left
        (1, 5, 20),    # Top-Front-Right  
        (2, 12, 16),   # Top-Back-Left
        (3, 13, 21),   # Top-Back-Right
        (8, 6, 18),    # Down-Front-Left
        (9, 7, 22),    # Down-Front-Right
        (10, 14, 18),  # Down-Back-Left
        (11, 15, 23)   # Down-Back-Right
    ]
    
    # Alternative mapping
    corners2 = [
        (0, 16, 4),
        (1, 4, 20),
        (2, 12, 17),
        (3, 21, 13),
        (8, 18, 6),
        (9, 6, 22),
        (10, 14, 19),
        (11, 23, 15)
    ]
    
    # Try to find which corner has the twisted pattern
    # by checking all possible corner definitions
    
    from collections import Counter
    
    for corner_def in [corners, corners2]:
        corner_sets = []
        for corner in corner_def:
            c_colors = tuple(sorted([colors[corner[0]], colors[corner[1]], colors[corner[2]]]))
            corner_sets.append(c_colors)
        
        freq = Counter(corner_sets)
        
        # Find the corner that appears odd number of times
        for corner_set, count in freq.items():
            if count % 2 == 1:
                print(''.join(corner_set))
                return
    
    # If no odd count found, return most common or least common
    corner_sets = []
    for corner in corners:
        c_colors = tuple(sorted([colors[corner[0]], colors[corner[1]], colors[corner[2]]]))
        corner_sets.append(c_colors)
    
    freq = Counter(corner_sets)
    result = min(freq.items(), key=lambda x: x[1])[0]
    print(''.join(result))

solve()
