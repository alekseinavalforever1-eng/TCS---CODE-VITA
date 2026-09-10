# Optimal Arrangement Problem Solution

## Problem Description
Bayland's environmental policy requires optimal arrangement of cargo ships to minimize transport costs. Goodies on land must be transported to their designated ships at sea.

## Problem Setup
- **Land**: Goodies positioned at 1km, 2km, 3km, ... from shore
- **Sea**: Ships positioned at 1km, 2km, 3km, ... from shore  
- **Distance Calculation**: `land_position + sea_position` (across the shore)
- **Cost Formula**: `weight × distance`

## Solution Approach

### 1. Input Processing
- Parse N goodies with their labels and weights
- Group goodies by ship labels (multiple goodies can have same label)
- Identify unique ships needed

### 2. Cost Calculation
For each ship arrangement:
- Assign ships to sea positions (1, 2, 3, ...)
- Calculate total cost: Σ(weight × (land_pos + sea_pos))

### 3. Optimization Strategy
- **Brute Force**: Try all permutations of ship arrangements
- **Find Minimum**: Identify all arrangements with minimum cost
- **Lexicographic Sorting**: Sort optimal arrangements alphabetically
- **Return Kth**: Output the Kth arrangement

### 4. Key Insights
- Distance is additive across shore: `land_position + sea_position`
- Multiple goodies can share the same ship label
- Need to find global minimum among all possible arrangements
- Handle ties by lexicographic ordering

## Algorithm Complexity
- **Time**: O(S! × N) where S = unique ships, N = total goodies
- **Space**: O(S! + N) for storing arrangements and goodie data

## Test Results

### Example 1: 8 goodies → 7 ships
```
Input: Diesel(1), Alloy(4), Battery(5), Alloy(1), Car(5), Zirconium(7), Vinyl(3), Wine(1)
K = 6
Output: 204, "Zirconium Battery Alloy Car Vinyl Wine Diesel"
```

### Example 2: 4 goodies → 3 ships  
```
Input: Can(5), Alloy(4), Battery(5), Alloy(1)
K = 3
Output: 62, "Battery Alloy Can"
```

## Implementation Details

### Distance Calculation
```python
# Goodies on land: positions 1, 2, 3, 4, ...
# Ships at sea: positions 1, 2, 3, ...
distance = land_position + sea_position
```

### Cost Optimization
```python
for arrangement in permutations(ship_labels):
    total_cost = 0
    for goodie in goodies:
        ship_pos = arrangement.index(goodie.label) + 1
        distance = goodie.land_pos + ship_pos
        total_cost += goodie.weight * distance
```

## Files
- `optimal_arrangement_final.py`: Complete solution
- `test_arrangement1.txt`, `test_arrangement2.txt`: Test cases
- `debug_*.py`: Development and verification utilities

## Usage
```bash
python3 optimal_arrangement_final.py < test_arrangement1.txt
```
