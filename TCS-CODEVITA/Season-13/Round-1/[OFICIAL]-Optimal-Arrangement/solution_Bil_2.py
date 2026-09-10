"""
Optimal Arrangement Problem - Final Solution
==========================================

Problem: Arrange cargo ships optimally to minimize transport costs for goodies.

Setup:
- Goodies are on land at positions 1km, 2km, 3km, ... from shore
- Ships are at sea at positions 1km, 2km, 3km, ... from shore  
- Distance = land_position + sea_position (across the shore)
- Cost = weight * distance
- Find Kth lexicographically sorted arrangement among all optimal solutions

Input:
- Line 1: N (number of goodies)
- Next N lines: label weight (goodie label and weight)
- Last line: K (Kth arrangement to return)

Output:
- Line 1: Minimum total cost
- Line 2: Kth optimal arrangement (space-separated ship labels)

Author: Solution for Bayland Environmental Policy
"""

from collections import defaultdict
from itertools import permutations

def solve():
    """Main solution function"""
    
    def calculate_total_cost(ship_arrangement, goodie_positions):
        """
        Calculate total transport cost for a given ship arrangement.
        
        Args:
            ship_arrangement (list): Order of ships from shore to sea
            goodie_positions (dict): {label: [(position, weight), ...]}
            
        Returns:
            int: Total transport cost
        """
        total_cost = 0
        
        # Create position mapping for ships (1-indexed from shore)
        ship_positions = {label: pos + 1 for pos, label in enumerate(ship_arrangement)}
        
        # Calculate cost for each goodie
        # Distance = land_position + sea_position (they're on opposite sides of shore)
        for label, positions in goodie_positions.items():
            ship_pos = ship_positions[label]
            for goodie_pos, weight in positions:
                distance = goodie_pos + ship_pos
                total_cost += weight * distance
                
        return total_cost
    
    def find_optimal_arrangements(ship_labels, goodie_positions):
        """
        Find all optimal ship arrangements that minimize total cost.
        
        Args:
            ship_labels (list): List of unique ship labels
            goodie_positions (dict): Positions and weights of goodies for each label
            
        Returns:
            tuple: (min_cost, list_of_optimal_arrangements)
        """
        min_cost = float('inf')
        optimal_arrangements = []
        
        # Try all possible permutations of ship arrangements
        for arrangement in permutations(ship_labels):
            cost = calculate_total_cost(arrangement, goodie_positions)
            
            if cost < min_cost:
                min_cost = cost
                optimal_arrangements = [list(arrangement)]
            elif cost == min_cost:
                optimal_arrangements.append(list(arrangement))
        
        return min_cost, optimal_arrangements
    
    # Read input
    n = int(input().strip())
    
    # Parse goodies and group by label
    goodie_positions = defaultdict(list)  # {label: [(position, weight), ...]}
    
    for i in range(n):
        line = input().strip().split()
        label = line[0]
        weight = int(line[1])
        
        # Goodie position is i+1 (1-indexed from shore)
        goodie_positions[label].append((i + 1, weight))
    
    k = int(input().strip())
    
    # Get unique ship labels
    ship_labels = list(goodie_positions.keys())
    
    # Find all optimal arrangements
    min_cost, optimal_arrangements = find_optimal_arrangements(ship_labels, goodie_positions)
    
    # Sort arrangements lexicographically
    optimal_arrangements.sort()
    
    # Get the Kth arrangement (1-indexed)
    kth_arrangement = optimal_arrangements[k - 1]
    
    # Output results
    print(min_cost)
    print(' '.join(kth_arrangement))

if __name__ == "__main__":
    solve()
