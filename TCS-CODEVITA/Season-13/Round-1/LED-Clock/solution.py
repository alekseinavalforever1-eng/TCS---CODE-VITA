def solve():
    LED_SEGMENTS = {
        0: {'a', 'b', 'c', 'd', 'e', 'f'},
        1: {'b', 'c'},
        2: {'a', 'b', 'd', 'e', 'g'},
        3: {'a', 'b', 'c', 'd', 'g'},
        4: {'b', 'c', 'f', 'g'},
        5: {'a', 'c', 'd', 'f', 'g'},
        6: {'a', 'c', 'd', 'e', 'f', 'g'},
        7: {'a', 'b', 'c'},
        8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        9: {'a', 'b', 'c', 'd', 'f', 'g'}
    }
    
    def can_transform(from_digit, to_digit):
        from_segments = LED_SEGMENTS[from_digit]
        to_segments = LED_SEGMENTS[to_digit]
        diff = len((from_segments - to_segments) | (to_segments - from_segments))
        return diff == 1
    
    def get_possible_digits(digit):
        result = []
        for target in range(10):
            if can_transform(digit, target):
                result.append(target)
        return result
    
    def is_valid_time(hours, minutes):
        return 1 <= hours <= 12 and 0 <= minutes <= 59
    
    def calculate_cost(initial_time, target_time, x, y):
        init_parts = initial_time.split(':')
        target_parts = target_time.split(':')
        init_h, init_m = int(init_parts[0]), int(init_parts[1])
        target_h, target_m = int(target_parts[0]), int(target_parts[1])
        
        minute_diff = abs(target_m - init_m)
        minute_cost = min(minute_diff, 60 - minute_diff) * y
        
        hour_diff = abs(target_h - init_h)
        hour_cost = min(hour_diff, 12 - hour_diff) * x
        
        return hour_cost + minute_cost
    
    initial_time = input().strip()
    x, y = map(int, input().strip().split())
    
    time_parts = initial_time.split(':')
    hours_str = time_parts[0]
    minutes_str = time_parts[1]
    
    h1, h2 = int(hours_str[0]), int(hours_str[1])
    m1, m2 = int(minutes_str[0]), int(minutes_str[1])
    
    possible_times = []
    
    # Try changing first hour digit
    for new_h1 in get_possible_digits(h1):
        new_hours = new_h1 * 10 + h2
        if is_valid_time(new_hours, int(minutes_str)):
            new_time = "{:02d}:{}".format(new_hours, minutes_str)
            possible_times.append(new_time)
    
    # Try changing second hour digit
    for new_h2 in get_possible_digits(h2):
        new_hours = h1 * 10 + new_h2
        if is_valid_time(new_hours, int(minutes_str)):
            new_time = "{:02d}:{}".format(new_hours, minutes_str)
            possible_times.append(new_time)
    
    # Try changing first minute digit
    for new_m1 in get_possible_digits(m1):
        new_minutes = new_m1 * 10 + m2
        if is_valid_time(int(hours_str), new_minutes):
            new_time = "{}:{:02d}".format(hours_str, new_minutes)
            possible_times.append(new_time)
    
    # Try changing second minute digit
    for new_m2 in get_possible_digits(m2):
        new_minutes = m1 * 10 + new_m2
        if is_valid_time(int(hours_str), new_minutes):
            new_time = "{}:{:02d}".format(hours_str, new_minutes)
            possible_times.append(new_time)
    
    # Remove duplicates
    unique_times = []
    for time in possible_times:
        if time not in unique_times:
            unique_times.append(time)
    
    if len(unique_times) == 0:
        print("No closest valid time possible")
        return
    
    min_cost = float('inf')
    best_time = None
    
    for time in unique_times:
        cost = calculate_cost(initial_time, time, x, y)
        if cost < min_cost:
            min_cost = cost
            best_time = time
    
    print(best_time)

solve()
