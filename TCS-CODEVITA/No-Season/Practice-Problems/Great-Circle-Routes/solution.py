# Problem: Great Circle Routes (Haversine Formula)
import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    lat1, lon1, lat2, lon2 = map(float, input_data[:4])
    R = 6371.0 # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    dist = R * c
    print(int(round(dist)))

if __name__ == "__main__":
    solve()
