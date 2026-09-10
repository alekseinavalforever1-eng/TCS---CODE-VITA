def solve():
    colors = input().split()
    
    # Correct 2x2 cube corner mappings
    # After analysis, the correct corners are:
    corners = [
        (0, 4, 17),   # Corner with indices that match cube geometry
        (1, 5, 20),
        (2, 4, 16),   # This might be the bry corner
        (3, 12, 21),
        (8, 6, 19),
        (9, 7, 22),
        (10, 15, 18),
        (11, 14, 23)
    ]
    
    # Alternative: use the correct standard mapping
    corners = [
        (0, 16, 4),
        (1, 4, 20),
        (2, 17, 12),
        (3, 12, 20),
        (8, 18, 6),
        (9, 6, 22),
        (10, 19, 14),
        (11, 14, 22)
    ]
    
    from collections import Counter
    
    corner_sets = []
    for corner in corners:
        c = tuple(sorted([colors[corner[0]], colors[corner[1]], colors[corner[2]]]))
        corner_sets.append(c)
    
    freq = Counter(corner_sets)
    
    # Find the one with count == 1 or odd count
    for color_combo, count in sorted(freq.items(), key=lambda x: x[1]):
        if count == 1:
            print(''.join(color_combo))
            return
    
    # Return least common
    min_count = min(freq.values())
    for color_combo, count in freq.items():
        if count == min_count:
            print(''.join(color_combo))
            return

solve()
