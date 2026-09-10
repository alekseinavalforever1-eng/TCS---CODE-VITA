import java.util.*;

public class Main {
    static int S;
    static char[][][] g;
    static boolean[][][] v;

    static class P {
        int l, r, c, d;

        public P(int l, int r, int c, int d) {
            this.l = l;
            this.r = r;
            this.c = c;
            this.d = d;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            S = sc.nextInt();
        } else {
            return;
        }

        g = new char[S][S][S];
        for (int l = 0; l < S; l++) {
            for (int r = 0; r < S; r++) {
                String ln = sc.next();
                for (int c = 0; c < S; c++) {
                    g[l][r][c] = ln.charAt(c);
                }
            }
        }

        int sl = sc.nextInt();
        int sr = sc.nextInt();
        int sc_ = sc.nextInt();

        int el = sc.nextInt();
        int er = sc.nextInt();
        int ec = sc.nextInt();

        System.out.print(bfs(sl, sr, sc_, el, er, ec));
    }

    static int bfs(int sl, int sr, int sc, int el, int er, int ec) {
        Queue<P> q = new LinkedList<>();
        v = new boolean[S][S][S];

        q.add(new P(sl, sr, sc, 0));
        v[sl][sr][sc] = true;

        while (!q.isEmpty()) {
            P cur = q.poll();

            if (cur.l == el && cur.r == er && cur.c == ec) {
                return cur.d;
            }

            List<int[]> n = gn(cur.l, cur.r, cur.c);

            for (int[] nx : n) {
                int nl = nx[0];
                int nr = nx[1];
                int nc = nx[2];

                if (!v[nl][nr][nc]) {
                    v[nl][nr][nc] = true;
                    q.add(new P(nl, nr, nc, cur.d + 1));
                }
            }
        }

        return -1;
    }

    static List<int[]> gn(int l, int r, int c) {
        List<int[]> n = new ArrayList<>();
        
        ao(l, r, c, n);

        cnd(l, r, c - 1, n);
        cnd(l, r, c + 1, n);
        cnd(l - 1, r, c, n);
        cnd(l + 1, r, c, n);

        cnt(l, r + 1, c + 1, 'L', n);
        cnt(l, r - 1, c - 1, 'L', n);

        cnt(l, r + 1, c - 1, 'R', n);
        cnt(l, r - 1, c + 1, 'R', n);

        cnt(l - 1, r - 1, c, 'F', n);
        cnt(l + 1, r + 1, c, 'F', n);

        cnt(l - 1, r + 1, c, 'B', n);
        cnt(l + 1, r - 1, c, 'B', n);

        return n;
    }

    static void ao(int l, int r, int c, List<int[]> n) {
        char t = g[l][r][c];
        
        if (t == 'D') {
            aiv(l, r, c - 1, n);
            aiv(l, r, c + 1, n);
            aiv(l - 1, r, c, n);
            aiv(l + 1, r, c, n);
        } else if (t == 'L') {
            aiv(l, r - 1, c - 1, n);
            aiv(l, r + 1, c + 1, n);
        } else if (t == 'R') {
            aiv(l, r - 1, c + 1, n);
            aiv(l, r + 1, c - 1, n);
        } else if (t == 'F') {
            aiv(l + 1, r + 1, c, n);
            aiv(l - 1, r - 1, c, n);
        } else if (t == 'B') {
            aiv(l + 1, r - 1, c, n);
            aiv(l - 1, r + 1, c, n);
        }
    }

    static void cnd(int l, int r, int c, List<int[]> n) {
        if (iv(l, r, c) && g[l][r][c] == 'D') {
            n.add(new int[]{l, r, c});
        }
    }

    static void cnt(int l, int r, int c, char t, List<int[]> n) {
        if (iv(l, r, c) && g[l][r][c] == t) {
            n.add(new int[]{l, r, c});
        }
    }

    static void aiv(int l, int r, int c, List<int[]> n) {
        if (iv(l, r, c)) {
            n.add(new int[]{l, r, c});
        }
    }

    static boolean iv(int l, int r, int c) {
        return l >= 0 && l < S && r >= 0 && r < S && c >= 0 && c < S && g[l][r][c] != 'E';
    }
}
