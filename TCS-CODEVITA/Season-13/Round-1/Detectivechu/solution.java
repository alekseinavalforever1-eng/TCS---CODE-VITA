import java.util.*;

public class TreasureHunt {
    static int N, M, K;
    static char[][] grid;
    static int[] values;
    static int startX, startY;
    
    static class State {
        int x, y, moves, treasure;
        long collected; // bitmask for collected cells
        
        State(int x, int y, int moves, int treasure, long collected) {
            this.x = x;
            this.y = y;
            this.moves = moves;
            this.treasure = treasure;
            this.collected = collected;
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        N = sc.nextInt();
        M = sc.nextInt();
        grid = new char[N][M];
        
        for (int i = 0; i < N; i++) {
            String line = sc.next();
            grid[i] = line.toCharArray();
        }
        
        startX = sc.nextInt();
        startY = sc.nextInt();
        
        values = new int[4];
        values[0] = sc.nextInt(); // Pearl ($)
        values[1] = sc.nextInt(); // Platinum (*)
        values[2] = sc.nextInt(); // Gold (%)
        values[3] = sc.nextInt(); // Diamond (+)
        
        K = sc.nextInt();
        
        System.out.println(solve());
    }
    
    static int solve() {
        Map<String, Integer> dp = new HashMap<>();
        PriorityQueue<State> pq = new PriorityQueue<>((a, b) -> b.treasure - a.treasure);
        
        int[] pos = applyGravity(startX, startY);
        int x = pos[0], moves = pos[1];
        
        if (moves > K || grid[x][startY] == '#') return 0;
        
        int initVal = getTreasureValue(grid[x][startY]);
        long initMask = (1L << (x * M + startY));
        pq.offer(new State(x, startY, K - moves, initVal, initMask));
        
        int maxTreasure = initVal;
        
        while (!pq.isEmpty()) {
            State curr = pq.poll();
            
            String key = curr.x + "," + curr.y + "," + curr.moves + "," + curr.collected;
            if (dp.containsKey(key) && dp.get(key) >= curr.treasure) continue;
            dp.put(key, curr.treasure);
            
            maxTreasure = Math.max(maxTreasure, curr.treasure);
            
            if (curr.moves == 0) continue;
            
            // Try left
            if (curr.y > 0) tryMove(curr, curr.x, curr.y - 1, pq);
            
            // Try right
            if (curr.y < M - 1) tryMove(curr, curr.x, curr.y + 1, pq);
            
            // Try up (climb)
            if (curr.x > 0 && canClimb(curr.x, curr.y)) {
                tryMove(curr, curr.x - 1, curr.y, pq);
            }
        }
        
        return maxTreasure;
    }
    
    static void tryMove(State curr, int newX, int newY, PriorityQueue<State> pq) {
        if (grid[newX][newY] == '#') return;
        
        int[] pos = applyGravity(newX, newY);
        int finalX = pos[0], slideMoves = pos[1];
        int totalMoves = 1 + slideMoves;
        
        if (curr.moves < totalMoves || grid[finalX][newY] == '#') return;
        
        int cellIdx = finalX * M + newY;
        long newMask = curr.collected;
        int newTreasure = curr.treasure;
        
        if ((curr.collected & (1L << cellIdx)) == 0) {
            newTreasure += getTreasureValue(grid[finalX][newY]);
            newMask |= (1L << cellIdx);
        }
        
        pq.offer(new State(finalX, newY, curr.moves - totalMoves, newTreasure, newMask));
    }
    
    static int[] applyGravity(int x, int y) {
        int moves = 0;
        while (x < N - 1 && grid[x + 1][y] != '#') {
            x++;
            moves++;
        }
        return new int[]{x, moves};
    }
    
    static boolean canClimb(int x, int y) {
        // Can climb if there's a rock below or adjacent
        if (x < N - 1 && grid[x + 1][y] == '#') return true;
        if (y > 0 && grid[x][y - 1] == '#') return true;
        if (y < M - 1 && grid[x][y + 1] == '#') return true;
        return false;
    }
    
    static int getTreasureValue(char c) {
        switch (c) {
            case '
: return values[0];
            case '*': return values[1];
            case '%': return values[2];
            case '+': return values[3];
            default: return 0;
        }
    }
}
