import java.util.*;

public class Main {
    
    static int N, M;
    static char[][] grid;
    static String word;
    static boolean[][] visited;
    static int I;

    static class Clue {
        int T, x1, y1, x2, y2;
    }

    static List<Clue> clues = new ArrayList<>();
    static int best = Integer.MAX_VALUE;

    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        grid = new char[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                grid[i][j] = sc.next().charAt(0);
            }
        }

        I = sc.nextInt();
        for (int k = 0; k < I; k++) {
            Clue c = new Clue();
            c.T = sc.nextInt();
            c.x1 = sc.nextInt() - 1;
            c.y1 = sc.nextInt() - 1;
            c.x2 = sc.nextInt() - 1;
            c.y2 = sc.nextInt() - 1;
            clues.add(c);
        }

        word = sc.next();

        visited = new boolean[N][M];

        boolean anyStart = false;

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                if (grid[r][c] == word.charAt(0)) {
                    anyStart = true;
                    int vio = violationAt(r, c, 1);
                    visited[r][c] = true;
                    dfs(r, c, 1, vio);
                    visited[r][c] = false;
                }
            }
        }

        if (!anyStart) {
            System.out.println("Impossible");
            return;
        }

        if (best == Integer.MAX_VALUE) {
            System.out.print("Impossible");
        } else if (best == 0) {
            System.out.print("All clues are correct");
        } else {
            System.out.print(best);
        }
    }

    static void dfs(int r, int c, int idx, int vio) {
        if (vio >= best) return;

        if (idx == word.length()) {
            best = Math.min(best, vio);
            return;
        }

        for (int k = 0; k < 4; k++) {
            int nr = r + dr[k];
            int nc = c + dc[k];

            if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
            if (visited[nr][nc]) continue;

            if (grid[nr][nc] != word.charAt(idx)) continue;

            visited[nr][nc] = true;

            int add = violationAt(nr, nc, idx + 1);
            dfs(nr, nc, idx + 1, vio + add);

            visited[nr][nc] = false;
        }
    }

    static int violationAt(int r, int c, int T) {
        int count = 0;
        for (Clue cl : clues) {
            if (cl.T == T) {
                if (cl.x1 <= r && r <= cl.x2 &&
                    cl.y1 <= c && c <= cl.y2) {
                    count++;
                }
            }
        }
        return count;
    }
}
