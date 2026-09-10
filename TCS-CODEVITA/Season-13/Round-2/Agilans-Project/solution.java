import java.util.*;

public class AgilansProject {

    static class Instruction {
        String turn;
        int dist;

        Instruction(String t, int d) {
            turn = t;
            dist = d;
        }
    }

    // Order of directions: 0 = North, 1 = East, 2 = South, 3 = West
    static final String[] DIRS = {"north", "east", "south", "west"};

    static final Map<String, Integer> TURN_CHANGE = new HashMap<>();
    static {
        TURN_CHANGE.put("left", -1);
        TURN_CHANGE.put("right", 1);
        TURN_CHANGE.put("straight", 0);
        TURN_CHANGE.put("back", 2);
    }

    static int mod4(int x) {
        x %= 4;
        if (x < 0) x += 4;
        return x;
    }

    // Simulates journey based on instructions
    static int[] simulate(List<Instruction> inst, int startDir, int startX, int startY) {
        int dir = startDir;
        int x = startX, y = startY;

        for (Instruction ins : inst) {
            dir = mod4(dir + TURN_CHANGE.get(ins.turn));

            if (dir == 0)      y += ins.dist; // North
            else if (dir == 1) x += ins.dist; // East
            else if (dir == 2) y -= ins.dist; // South
            else if (dir == 3) x -= ins.dist; // West
        }
        return new int[]{x, y};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine().trim());
        List<Instruction> inst = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String[] parts = sc.nextLine().trim().split(" ");
            inst.add(new Instruction(parts[0], Integer.parseInt(parts[1])));
        }

        int startX = sc.nextInt();
        int startY = sc.nextInt();
        int targetX = sc.nextInt();
        int targetY = sc.nextInt();

        sc.close();

        boolean found = false;

        // Try changing each instruction once
        for (int i = 0; i < N && !found; i++) {
            String wrongTurn = inst.get(i).turn;
            int dist = inst.get(i).dist;

            for (String candidate : TURN_CHANGE.keySet()) {
                if (candidate.equals(wrongTurn)) continue;

                List<Instruction> modified = new ArrayList<>();
                for (int k = 0; k < N; k++) {
                    if (k == i) modified.add(new Instruction(candidate, dist));
                    else modified.add(inst.get(k));
                }

                int[] endPos = simulate(modified, 0, startX, startY);

                if (endPos[0] == targetX && endPos[1] == targetY) {
                    System.out.println("Yes");
                    System.out.println(wrongTurn + " " + dist);
                    System.out.println(candidate + " " + dist);
                    found = true;
                    break;
                }
            }
        }

        if (!found) {
            System.out.println("No");
        }
    }
}
