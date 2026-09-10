import java.util.*;
public class Main {
    static int R, C, M, N, K, B, T;
    static char[][] G;
    static Map<Character, Integer> P;
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        if (!s.hasNext()) return;
        R = s.nextInt(); C = s.nextInt(); M = s.nextInt();
        G = new char[R][C];
        for (char[] r : G) Arrays.fill(r, '.');
        for (int i = 0; i < M; i++)
            for (int j = 0; j < C; j++) G[R - 1 - i][j] = s.next().charAt(0);
        if (s.hasNextLine()) s.nextLine();
        String[] c = s.nextLine().trim().split("\\s+"), p = s.nextLine().trim().split("\\s+");
        P = new HashMap<>();
        for (int i = 0; i < c.length; i++) if (i < p.length) P.put(c[i].charAt(0), Integer.parseInt(p[i]));
        N = s.nextInt(); K = s.nextInt();
        solve();
        System.out.println(T);
    }
    static void solve() {
        int r = 0, c = N, dr = 1, dc = -1, st = 0;
        while (B < K && st < 10000) {
            if (clr()) break;
            int nr = r + dr, nc = c + dc;
            if (nr < 0 || nr >= R || nc < 0 || nc >= C) {
                if (nr < 0 || nr >= R) dr = -dr;
                if (nc < 0 || nc >= C) dc = -dc;
                nr = r + dr; nc = c + dc;
            }
            List<int[]> h = new ArrayList<>();
            boolean v = ok(r + dr, c) && G[r + dr][c] != '.', hz = ok(r, c + dc) && G[r][c + dc] != '.';
            if (v) h.add(new int[]{r + dr, c});
            if (hz) h.add(new int[]{r, c + dc});
            if (v || hz) {
                B++; proc(h, false); st = 0;
                if (v && hz) { dr = -dr; dc = -dc; }
                else { if (v) dr = -dr; if (hz) dc = -dc; }
                continue;
            }
            if (ok(nr, nc) && G[nr][nc] != '.') {
                B++; h.add(new int[]{nr, nc}); proc(h, true); st = 0;
                dr = -dr; dc = -dc;
                continue;
            }
            r = nr; c = nc; st++;
        }
    }
    static void proc(List<int[]> h, boolean d) {
        Set<String> b = new HashSet<>();
        for (int[] p : h) if (G[p[0]][p[1]] != '.') bfs(p[0], p[1], G[p[0]][p[1]], b, d);
        for (String s : b) { String[] x = s.split(","); G[Integer.parseInt(x[0])][Integer.parseInt(x[1])] = '.'; }
        Set<String> sp = new HashSet<>();
        Queue<int[]> q = new LinkedList<>();
        for (int j = 0; j < C; j++) if (G[R - 1][j] != '.') { sp.add((R - 1) + "," + j); q.add(new int[]{R - 1, j}); }
        boolean[][] v = new boolean[R][C];
        for (int[] p : q) v[p[0]][p[1]] = true;
        while (!q.isEmpty()) {
            int[] u = q.poll();
            int cr = u[0], cc = u[1];
            char k = G[cr][cc];
            check(cr - 1, cc, sp, q, v, '.', false);
            check(cr, cc - 1, sp, q, v, k, true);
            check(cr, cc + 1, sp, q, v, k, true);
        }
        for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) if (G[i][j] != '.' && !sp.contains(i + "," + j)) {
            if (P.containsKey(G[i][j])) T += P.get(G[i][j]);
            G[i][j] = '.';
        }
    }
    static void check(int r, int c, Set<String> s, Queue<int[]> q, boolean[][] v, char k, boolean m) {
        if (ok(r, c) && G[r][c] != '.' && !v[r][c]) {
            if (m && G[r][c] != k) return;
            v[r][c] = true; s.add(r + "," + c); q.add(new int[]{r, c});
        }
    }
    static void bfs(int r, int c, char k, Set<String> b, boolean d) {
        Queue<int[]> q = new LinkedList<>(); q.add(new int[]{r, c}); b.add(r + "," + c);
        while (!q.isEmpty()) {
            int[] u = q.poll();
            int[][] ds = (d && u[0] == r && u[1] == c) ? new int[][]{{0, 1}, {0, -1}} : new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
            for (int[] dir : ds) {
                int nr = u[0] + dir[0], nc = u[1] + dir[1];
                if (ok(nr, nc) && G[nr][nc] == k && b.add(nr + "," + nc)) q.add(new int[]{nr, nc});
            }
        }
    }
    static boolean ok(int r, int c) { return r >= 0 && r < R && c >= 0 && c < C; }
    static boolean clr() { for (char[] r : G) for (char c : r) if (c != '.') return false; return true; }
}
