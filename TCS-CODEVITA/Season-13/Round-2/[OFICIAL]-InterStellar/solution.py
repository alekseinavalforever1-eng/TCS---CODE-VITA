from collections import deque
M = 50
def P(d):
    if d == 0: return [(0,0)]
    s = []
    s += [(0,1)]*d
    s += [(-1,0)]*(2*d)
    s += [(0,-1)]*(2*d)
    s += [(1,0)]*(2*d)
    s += [(0,1)]*d
    x,y = d,0
    r = [(x,y)]
    for a,b in s:
        x += a; y += b
        r.append((x,y))
    return r[:-1]

def C(pm,rd,root,pts,T=M):
    per = {}; dval = {}
    for z in pts:
        r = rd.get(z,1)
        d = max(0,r-1)
        if z == root: d = 0
        dval[z] = d
        per[z] = P(d)
    par = {z:pm.get(z,None) for z in pts}
    pos = {z:[None]*(T+1) for z in pts}
    def G(z,t):
        if pos[z][t] is not None: return pos[z][t]
        pz = par[z]
        base = (0,0) if pz is None else G(pz,t)
        d = dval[z]
        off = (0,0) if d==0 else per[z][t % len(per[z])]
        pos[z][t] = (base[0]+off[0], base[1]+off[1])
        return pos[z][t]
    for z in pts:
        for t in range(T+1):
            G(z,t)
    return pos

def S(rel,src,dst):
    pts = set(); child = set(); pm = {}; rd = {}
    for a,b,r in rel:
        pts.add(a); pts.add(b)
        child.add(a)
        pm[a] = b
        rd[a] = int(r)
    rootset = pts - child
    root = next(iter(rootset)) if rootset else None
    if root and root not in rd: rd[root]=1
    for z in pts:
        if z not in rd: rd[z]=1
    pts = sorted(pts)
    pos = C(pm,rd,root,pts,T=M)
    xs = []; ys = []
    for z in pts:
        for t in range(M+1):
            x,y = pos[z][t]; xs.append(x); ys.append(y)
    lx,rx = min(xs)-1, max(xs)+1
    ly,ry = min(ys)-1, max(ys)+1
    lx -= M; rx += M; ly -= M; ry += M
    dest = {t: pos[dst][t] for t in range(M+1)}
    q = deque()
    vis = set()
    sx,sy = pos[src][0]
    q.append((sx,sy,0)); vis.add((sx,sy,0))
    moves = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        x,y,t = q.popleft()
        if (x,y) == dest[t]:
            return t
        if t >= M: continue
        nt = t+1
        for dx,dy in moves:
            nx,ny = x+dx, y+dy
            if nx<lx or nx>rx or ny<ly or ny>ry: continue
            st = (nx,ny,nt)
            if st in vis: continue
            vis.add(st); q.append(st)
    return None

def solve(s):
    a = [ln.strip() for ln in s.strip().splitlines() if ln.strip()]
    n = int(a[0])
    rel = []
    for i in range(1,n+1):
        x,y,z = a[i].split(); rel.append((x,y,int(z)))
    src,dst = a[n+1].split()
    ans = S(rel,src,dst)
    print(ans if ans is not None else -1,end="")

if __name__ == "__main__":
    import sys
    data = sys.stdin.read()
    solve(data)
