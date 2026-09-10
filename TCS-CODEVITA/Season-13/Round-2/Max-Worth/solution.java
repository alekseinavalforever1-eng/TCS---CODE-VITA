import java.util.*;

public class MaxWorth {

    static int N, M, budget;
    static int[] costs, worths;
    static boolean[][] conflict;

    // Compact memo with a proper key type (no string concatenation; no bit packing collisions)
    static class Key {
        final int idx, remBudget;
        final long usedMask;
        Key(int idx, long usedMask, int remBudget) {
            this.idx = idx; this.usedMask = usedMask; this.remBudget = remBudget;
        }
        @Override public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Key)) return false;
            Key k = (Key) o;
            return idx == k.idx && remBudget == k.remBudget && usedMask == k.usedMask;
        }
        @Override public int hashCode() {
            int h = idx;
            h = 31 * h + remBudget;
            h = 31 * h + (int)(usedMask ^ (usedMask >>> 32));
            return h;
        }
    }
    static Map<Key, Integer> memo = new HashMap<>();

    static int calcWorth(String s) {
        int sum = 0;
        for (char ch : s.toCharArray()) sum += (ch - 'a' + 1);
        return sum;
    }

    static int dfs(int idx, long usedMask, int remBudget) {
        if (idx == N) return 0;

        Key key = new Key(idx, usedMask, remBudget);
        Integer cached = memo.get(key);
        if (cached != null) return cached;

        // Option 1: skip
        int best = dfs(idx + 1, usedMask, remBudget);

        // Option 2: take (if budget allows and no conflict)
        if (costs[idx] <= remBudget) {
            boolean ok = true;
            for (int k = 0; k < N; k++) {
                if (((usedMask >>> k) & 1L) != 0L && conflict[idx][k]) {
                    ok = false; break;
                }
            }
            if (ok) {
                best = Math.max(best,
                        worths[idx] + dfs(idx + 1, usedMask | (1L << idx), remBudget - costs[idx]));
            }
        }

        memo.put(key, best);
        return best;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        String[] strings = new String[N];
        for (int i = 0; i < N; i++) strings[i] = sc.next();

        costs = new int[N];
        for (int i = 0; i < N; i++) costs[i] = sc.nextInt();

        worths = new int[N];
        for (int i = 0; i < N; i++) worths[i] = calcWorth(strings[i]);

        Map<String, Integer> index = new HashMap<>();
        for (int i = 0; i < N; i++) index.put(strings[i], i);

        conflict = new boolean[N][N];
        for (int i = 0; i < M; i++) {
            String a = sc.next();
            String b = sc.next();
            int ai = index.get(a), bi = index.get(b);
            conflict[ai][bi] = true;
            conflict[bi][ai] = true;
        }

        budget = sc.nextInt();

        System.out.println(dfs(0, 0L, budget));
        sc.close();
    }
}
