import sys, math
EPS = 1e-9

def side_of_line(p1, p2, q):
    return (p2[0]-p1[0])*(q[1]-p1[1]) - (p2[1]-p1[1])*(q[0]-p1[0])

def seg_line_intersection(a, b, p1, p2):
    ax,ay = a; bx,by = b
    p1x,p1y = p1; p2x,p2y = p2
    r = (bx-ax, by-ay)
    s = (p2x-p1x, p2y-p1y)
    denom = r[0]*s[1] - r[1]*s[0]
    if abs(denom) < EPS: return None
    t = ((p1x-ax)*s[1] - (p1y-ay)*s[0]) / denom
    return (ax + t*r[0], ay + t*r[1])

def clip_polygon_with_halfplane(poly, p1, p2, keep_left=True):
    res = []
    n = len(poly)
    for i in range(n):
        A = poly[i]
        B = poly[(i+1)%n]
        sa = side_of_line(p1,p2,A)
        sb = side_of_line(p1,p2,B)
        if keep_left:
            insideA = sa >= -EPS
            insideB = sb >= -EPS
        else:
            insideA = sa <= EPS
            insideB = sb <= EPS
        if insideA and insideB:
            res.append(B)
        elif insideA and not insideB:
            ip = seg_line_intersection(A,B,p1,p2)
            if ip: res.append(ip)
        elif not insideA and insideB:
            ip = seg_line_intersection(A,B,p1,p2)
            if ip: res.append(ip)
            res.append(B)
    out = []
    for p in res:
        if not out or (abs(out[-1][0]-p[0])>1e-8 or abs(out[-1][1]-p[1])>1e-8):
            out.append(p)
    if len(out)>1 and abs(out[0][0]-out[-1][0])<1e-8 and abs(out[0][1]-out[-1][1])<1e-8:
        out.pop()
    return out

def reflect_point_about_line(p, a, b):
    ax,ay = a; bx,by = b; px,py = p
    vx = bx-ax; vy = by-ay
    norm2 = vx*vx + vy*vy
    if norm2 < EPS: return p
    apx = px-ax; apy = py-ay
    t = (apx*vx + apy*vy) / norm2
    projx = ax + t*vx; projy = ay + t*vy
    rx = 2*projx - px
    ry = 2*projy - py
    return (rx, ry)

def segment_intersection(s1a, s1b, s2a, s2b):
    ax,ay = s1a; bx,by = s1b; cx,cy = s2a; dx,dy = s2b
    r = (bx-ax, by-ay)
    s = (dx-cx, dy-cy)
    denom = r[0]*s[1] - r[1]*s[0]
    def on_segment(p,q,rp):
        return (min(p[0],rp[0]) - EPS <= q[0] <= max(p[0],rp[0]) + EPS and
                min(p[1],rp[1]) - EPS <= q[1] <= max(p[1],rp[1]) + EPS)
    if abs(denom) < EPS:
        if abs((cx-ax)*r[1] - (cy-ay)*r[0]) < EPS:
            for pt in (s1a, s1b, s2a, s2b):
                if on_segment(s1a, pt, s1b) and on_segment(s2a, pt, s2b):
                    return pt
        return None
    t = ((cx-ax)*s[1] - (cy-ay)*s[0]) / denom
    u = ((cx-ax)*r[1] - (cy-ay)*r[0]) / denom
    if -EPS <= t <= 1+EPS and -EPS <= u <= 1+EPS:
        return (ax + t*r[0], ay + t*r[1])
    return None

def unique_points(points):
    uniq = []
    for p in points:
        found = False
        for q in uniq:
            if abs(p[0]-q[0])<1e-6 and abs(p[1]-q[1])<1e-6:
                found = True; break
        if not found: uniq.append(p)
    return uniq

def point_in_poly(pt, poly):
    x,y = pt
    inside = False
    n = len(poly)
    if n == 0: return False
    for i in range(n):
        x1,y1 = poly[i]; x2,y2 = poly[(i+1)%n]
        if (min(x1,x2)-EPS <= x <= max(x1,x2)+EPS and min(y1,y2)-EPS <= y <= max(y1,y2)+EPS):
            if abs((x2-x1)*(y-y1) - (y2-y1)*(x-x1)) < 1e-8: return True
        if ((y1>y) != (y2>y)) and (x < (x2-x1)*(y-y1)/(y2-y1+1e-30) + x1):
            inside = not inside
    return inside

def is_inside_union(pt, right_poly, left_ref):
    return point_in_poly(pt, right_poly) or point_in_poly(pt, left_ref)

def is_on_union_boundary(pt, right_poly, left_ref):
    inside_flags = []
    r = 1e-4
    for k in range(8):
        ang = 2*math.pi*k/8.0
        q = (pt[0] + r*math.cos(ang), pt[1] + r*math.sin(ang))
        inside_flags.append(is_inside_union(q, right_poly, left_ref))
    if any(inside_flags) and not all(inside_flags): return True
    for poly in (right_poly, left_ref):
        for i in range(len(poly)):
            a = poly[i]; b = poly[(i+1)%len(poly)]
            ax,ay=a; bx,by=b; px,py=pt
            vx=bx-ax; vy=by-ay
            seglen2 = vx*vx+vy*vy
            if seglen2 < EPS: continue
            t = ((px-ax)*vx + (py-ay)*vy)/seglen2
            t = max(0.0, min(1.0, t))
            proj = (ax + t*vx, ay + t*vy)
            dist2 = (proj[0]-px)**2 + (proj[1]-py)**2
            if dist2 < 1e-8:
                ang = math.atan2(vy, vx) + math.pi/2
                q_out = (pt[0] + 1e-4*math.cos(ang), pt[1] + 1e-4*math.sin(ang))
                if not is_inside_union(q_out, right_poly, left_ref):
                    return True
    return False

def edges(poly):
    return [ (poly[i], poly[(i+1)%len(poly)]) for i in range(len(poly)) ] if len(poly)>=2 else []

def process(area, x1,y1,x2,y2):
    s = math.sqrt(area)
    square = [(0.0,0.0),(0.0,s),(s,s),(s,0.0)]
    p1 = (float(x1),float(y1)); p2 = (float(x2),float(y2))
    left_poly = clip_polygon_with_halfplane(square,p1,p2,keep_left=True)
    right_poly = clip_polygon_with_halfplane(square,p1,p2,keep_left=False)
    left_ref = [reflect_point_about_line(p,p1,p2) for p in left_poly]
    pts = []
    for p in right_poly: pts.append(p)
    for p in left_ref: pts.append(p)
    for e1 in edges(right_poly):
        for e2 in edges(left_ref):
            ip = segment_intersection(e1[0], e1[1], e2[0], e2[1])
            if ip: pts.append(ip)
    uniq = unique_points(pts)
    filtered = []
    for p in uniq:
        if is_on_union_boundary(p, right_poly, left_ref):
            filtered.append(p)
    filtered_sorted = sorted(filtered, key=lambda p:(round(p[0],10), round(p[1],10)))
    return filtered_sorted

def main():
    data = sys.stdin.read().strip().split()
    if not data: 
        return
    area = float(data[0])
    x1,y1,x2,y2 = map(float, data[1:5])
    res = process(area,x1,y1,x2,y2)
    rounded = []
    seen = set()
    for x,y in sorted(res, key=lambda p:(p[0],p[1])):
        rx = round(x+0.0, 2) 
        ry = round(y+0.0, 2)
        key = (f"{rx:.2f}", f"{ry:.2f}")
        if key in seen: continue
        seen.add(key)
        rounded.append(key)
    out_lines = [f"{a} {b}" for (a,b) in rounded]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
