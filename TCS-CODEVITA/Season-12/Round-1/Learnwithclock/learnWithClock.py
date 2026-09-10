def calc_cost(a, h, m, A, B, P, Q, X, Y):
    cur_angle = abs((h * 30 + m * 0.5) - (m * 6))
    cur_angle = min(cur_angle, 360 - cur_angle)
    diff = abs(a - cur_angle)
    diff = min(diff, 360 - diff)

    costs = []
    
   
    if h < 11:
        costs.append((30 * P if diff <= 90 else (30 * P + (diff - 90) * Q)))
    
   
    if h > 0:
        costs.append((30 * P if diff <= 90 else (30 * P + (diff - 90) * Q)))

  
    costs.append((diff * X if diff <= 90 else (90 * X + (diff - 90) * Y)))

   
    costs.append(diff * B)

    return min(costs)

def proc_queries(t, qs, c):
    h, m = map(int, t.split(':'))
    total_cost = sum(calc_cost(q, h, m, *c) for q in qs)
    return total_cost


t = input().strip()
N = int(input().strip())
A, B = map(int, input().strip().split())
P, Q = map(int, input().strip().split())
X, Y = map(int, input().strip().split())
qs = [int(input().strip()) for _ in range(N)]

costs = [A, B, P, Q, X, Y]
result = proc_queries(t, qs, costs)
print(result)
