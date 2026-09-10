def solve_led_clock():
    """
    Solve the LED clock problem by finding the closest valid time
    that can be formed by toggling exactly one LED segment.
    """
    
    # LED segment representation for digits 0-9
    # Each digit represented as a set of segments (a, b, c, d, e, f, g)
    #   a
    #  f b
    #   g
    #  e c
    #   d
    
    led_segments = {
        0: {'a', 'b', 'c', 'd', 'e', 'f'},        # 0
        1: {'b', 'c'},                             # 1
        2: {'a', 'b', 'd', 'e', 'g'},             # 2
        3: {'a', 'b', 'c', 'd', 'g'},             # 3
        4: {'b', 'c', 'f', 'g'},                  # 4
        5: {'a', 'c', 'd', 'f', 'g'},             # 5
        6: {'a', 'c', 'd', 'e', 'f', 'g'},        # 6
        7: {'a', 'b', 'c'},                       # 7
        8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},   # 8
        9: {'a', 'b', 'c', 'd', 'f', 'g'}         # 9
    }
    
    def can_transform_by_one_toggle(from_digit, to_digit):
        """Check if we can transform from_digit to to_digit by toggling exactly one segment"""
        from_segments = led_segments[from_digit]
        to_segments = led_segments[to_digit]
        
        # Find segments that need to be turned on or off
        segments_to_turn_on = to_segments - from_segments
        segments_to_turn_off = from_segments - to_segments
        
        # Exactly one segment should be toggled (either on or off, but not both)
        total_changes = len(segments_to_turn_on) + len(segments_to_turn_off)
        return total_changes == 1
    
    def get_possible_digits(digit):
        """Get all digits that can be formed by toggling exactly one segment from the given digit"""
        possible = []
        for target_digit in range(10):
            if can_transform_by_one_toggle(digit, target_digit):
                possible.append(target_digit)
        return possible
    
    def is_valid_time(hours, minutes):
        """Check if the given time is valid"""
        return 1 <= hours <= 12 and 0 <= minutes <= 59
    
    def calculate_cost(initial_time, target_time, x, y):
        """Calculate the cost to move clock hands from initial_time to target_time"""
        init_h, init_m = map(int, initial_time.split(':'))
        target_h, target_m = map(int, target_time.split(':'))
        
        # Calculate minute hand movement cost
        minute_diff = abs(target_m - init_m)
        minute_cost = min(minute_diff, 60 - minute_diff) * y
        
        # Calculate hour hand movement cost
        hour_diff = abs(target_h - init_h)
        hour_cost = min(hour_diff, 12 - hour_diff) * x
        
        return hour_cost + minute_cost
    
    def generate_possible_times(initial_time):
        """Generate all possible times by toggling exactly one LED segment"""
        hours, minutes = initial_time.split(':')
        h1, h2 = int(hours[0]), int(hours[1])
        m1, m2 = int(minutes[0]), int(minutes[1])
        
        possible_times = []
        
        # Try changing first hour digit
        for new_h1 in get_possible_digits(h1):
            new_hours = new_h1 * 10 + h2
            if is_valid_time(new_hours, int(minutes)):
                possible_times.append(f"{new_hours:02d}:{minutes}")
        
        # Try changing second hour digit
        for new_h2 in get_possible_digits(h2):
            new_hours = h1 * 10 + new_h2
            if is_valid_time(new_hours, int(minutes)):
                possible_times.append(f"{new_hours:02d}:{minutes}")
        
        # Try changing first minute digit
        for new_m1 in get_possible_digits(m1):
            new_minutes = new_m1 * 10 + m2
            if is_valid_time(int(hours), new_minutes):
                possible_times.append(f"{hours}:{new_minutes:02d}")
        
        # Try changing second minute digit
        for new_m2 in get_possible_digits(m2):
            new_minutes = m1 * 10 + new_m2
            if is_valid_time(int(hours), new_minutes):
                possible_times.append(f"{hours}:{new_minutes:02d}")
        
        return list(set(possible_times))  # Remove duplicates
    
    # Read input
    initial_time = input().strip()
    x, y = map(int, input().split())
    
    # Generate all possible times
    possible_times = generate_possible_times(initial_time)
    
    if not possible_times:
        print("No closest valid time possible")
        return
    
    # Find the time with minimum cost
    min_cost = float('inf')
    closest_time = None
    
    for time in possible_times:
        cost = calculate_cost(initial_time, time, x, y)
        if cost < min_cost:
            min_cost = cost
            closest_time = time
    
    if closest_time:
        print(closest_time)
    else:
        print("No closest valid time possible")

if __name__ == "__main__":
    solve_led_clock()
