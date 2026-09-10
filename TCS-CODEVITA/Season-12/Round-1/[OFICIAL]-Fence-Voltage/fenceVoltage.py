def compute_voltage(wire_segments):
    from collections import defaultdict

    
    intersection_voltage = defaultdict(int)

   
    segments = []

    for start_x, start_y, end_x, end_y in wire_segments:
        if start_x == end_x:  # Vertical segment
            for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                segments.append((start_x, y))
                intersection_voltage[(start_x, y)] += 1
        else:  # Horizontal segment
            for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
                segments.append((x, start_y))
                intersection_voltage[(x, start_y)] += 1

    total_voltage = 0

    for point in intersection_voltage:
        wire_count = intersection_voltage[point]
        min_cells = float('inf')

        # Calculate minimum cells touched by wires at this intersection
        for (x1, y1, x2, y2) in wire_segments:
            if (x1 == x2 and point[0] == x1) or (y1 == y2 and point[1] == y1):
                if x1 == x2:  # Vertical wire
                    distance = abs(point[1] - y1)
                    min_cells = min(min_cells, distance)
                else:  # Horizontal wire
                    distance = abs(point[0] - x1)
                    min_cells = min(min_cells, distance)

        total_voltage += wire_count * min_cells

    return total_voltage


def check_animal_status(voltage, animal_limits, animal_name):
    threshold = animal_limits.get(animal_name)
    
    if threshold is None:
        return "No", 0.0

    is_dead = voltage >= threshold
    return "Yes" if is_dead else "No", None


def calculate_death_probability(animal_limits, total_voltage):
    dead_count = sum(1 for threshold in animal_limits.values() if total_voltage >= threshold)
    total_animals = len(animal_limits)
    
    return round(dead_count / total_animals, 2)



num_wires = int(input())
wire_segments = [tuple(map(int, input().split())) for _ in range(num_wires)]
animal_info = input().strip().split()
animal_limits = {data.split(':')[0]: int(data.split(':')[1]) for data in animal_info}
touched_animal = input().strip()


total_voltage = compute_voltage(wire_segments)


animal_status, _ = check_animal_status(total_voltage, animal_limits, touched_animal)
death_probability = calculate_death_probability(animal_limits, total_voltage)


print(animal_status)
print(death_probability)
