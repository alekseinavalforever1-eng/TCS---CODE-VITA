import java.util.*;

public class FaultySegment {
    static Map<String, Character> segMap = new HashMap<>();
    static int N;

    // Build dictionary
    static void buildMap() {
        segMap.put(" _ | ||_|", '0');
        segMap.put("     |  |", '1');
        segMap.put(" _  _||_ ", '2');
        segMap.put(" _  _| _|", '3');
        segMap.put("   |_|  |", '4');
        segMap.put(" _ |_  _|", '5');
        segMap.put(" _ |_ |_|", '6');
        segMap.put(" _   |  |", '7');
        segMap.put(" _ |_||_|", '8');
        segMap.put(" _ |_| _|", '9');

        // operators (placeholders, adjust from problem images)
        segMap.put("   _     ", '-');
        segMap.put("         ", '+'); 
        segMap.put("         ", '*'); 
        segMap.put("         ", '%'); 
        segMap.put("         ", '='); 
    }

    // Extract characters from the 3 lines
    static String[] extract(String[] rows) {
        String[] blocks = new String[N];
        for (int i = 0; i < N; i++) {
            StringBuilder sb = new StringBuilder();
            for (int r = 0; r < 3; r++) {
                int start = i * 3;
                sb.append(rows[r].substring(start, start + 3));
            }
            blocks[i] = sb.toString();
        }
        return blocks;
    }

    // Convert list of characters into integer value
    static int parseNum(List<Character> chars) {
        StringBuilder sb = new StringBuilder();
        for (char c : chars) sb.append(c);
        return Integer.parseInt(sb.toString());
    }

    // Evaluate expression left-to-right (no precedence)
    static int evaluate(List<Character> expr) {
        List<Integer> nums = new ArrayList<>();
        List<Character> ops = new ArrayList<>();

        StringBuilder num = new StringBuilder();
        for (char c : expr) {
            if (Character.isDigit(c)) {
                num.append(c);
            } else {
                nums.add(Integer.parseInt(num.toString()));
                num.setLength(0);
                ops.add(c);
            }
        }
        nums.add(Integer.parseInt(num.toString()));

        int val = nums.get(0);
        for (int i = 0; i < ops.size(); i++) {
            char op = ops.get(i);
            int b = nums.get(i + 1);
            if (op == '+') val += b;
            else if (op == '-') val -= b;
            else if (op == '*') val *= b;
            else if (op == '%') val %= b;
        }
        return val;
    }

    // Check if toggling one LED in block i fixes equation
    static boolean check(String[] blocks, int idx) {
        char[] arr = blocks[idx].toCharArray();
        for (int pos = 0; pos < arr.length; pos++) {
            char old = arr[pos];
            arr[pos] = (old == ' ') ? '_' : ' '; // toggle
            String newBlock = new String(arr);

            if (segMap.containsKey(newBlock)) {
                char fixedChar = segMap.get(newBlock);

                // rebuild full expression
                List<Character> left = new ArrayList<>();
                List<Character> right = new ArrayList<>();
                boolean eqSeen = false;

                for (int i = 0; i < N; i++) {
                    String blk = (i == idx ? newBlock : blocks[i]);
                    if (!segMap.containsKey(blk)) {
                        eqSeen = true; // skip unknowns
                        continue;
                    }
                    char c = segMap.get(blk);
                    if (c == '=') { eqSeen = true; continue; }
                    if (!eqSeen) left.add(c);
                    else right.add(c);
                }

                try {
                    int lhs = evaluate(left);
                    int rhs = parseNum(right);
                    if (lhs == rhs) return true;
                } catch (Exception e) {
                    // ignore invalid parses
                }
            }
            arr[pos] = old; // revert
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = Integer.parseInt(sc.nextLine().trim());

        String[] rows = new String[3];
        for (int i = 0; i < 3; i++) {
            rows[i] = sc.nextLine();
            while (rows[i].length() < N * 3) rows[i] += " ";
        }

        buildMap();
        String[] blocks = extract(rows);

        for (int i = 0; i < N; i++) {
            if (check(blocks, i)) {
                System.out.println(i + 1);
                return;
            }
        }
    }
}
