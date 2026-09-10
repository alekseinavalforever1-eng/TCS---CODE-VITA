import java.util.*;

public class Main1 {
    static Map<String, List<List<String>>> recipes = new HashMap<>();
    static Map<String, Integer> memo = new HashMap<>();

    // Function to compute minimum orbs required for potion
    static int dfs(String potion) {
        if (memo.containsKey(potion)) return memo.get(potion);

        // If potion is not in recipes => it's a base item, cost = 0
        if (!recipes.containsKey(potion)) return 0;

        int minOrbs = Integer.MAX_VALUE;

        for (List<String> ingredients : recipes.get(potion)) {
            int cost = ingredients.size() - 1; // orbs for combining
            boolean valid = true;
            for (String ing : ingredients) {
                int sub = dfs(ing);
                if (sub == Integer.MAX_VALUE) {
                    valid = false;
                    break;
                }
                cost += sub;
            }
            if (valid) minOrbs = Math.min(minOrbs, cost);
        }

        memo.put(potion, minOrbs);
        return minOrbs;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < N; i++) {
            String line = sc.nextLine();
            String[] parts = line.split("=");
            String result = parts[0];
            String[] ing = parts[1].split("\\+");

            recipes.putIfAbsent(result, new ArrayList<>());
            recipes.get(result).add(Arrays.asList(ing));
        }

        String target = sc.nextLine().trim();
        int ans = dfs(target);

        if (ans == Integer.MAX_VALUE) ans = -1; // unreachable case
        System.out.println(ans);
    }
}
