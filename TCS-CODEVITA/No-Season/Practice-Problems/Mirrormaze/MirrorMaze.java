import java.util.*;

public class MirrorMaze {
    
    static class State {
        int row, col, dir;
        
        State(int row, int col, int dir) {
            this.row = row;
            this.col = col;
            this.dir = dir;
        }
        
        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            State state = (State) obj;
            return row == state.row && col == state.col && dir == state.dir;
        }
        
        @Override
        public int hashCode() {
            return Objects.hash(row, col, dir);
        }
    }
    
    // Directions: 0=Right, 1=Down, 2=Left, 3=Up
    static int[] dr = {0, 1, 0, -1};
    static int[] dc = {1, 0, -1, 0};
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int M = sc.nextInt();
        int N = sc.nextInt();
        sc.nextLine(); // consume newline
        
        char[][] grid = new char[M][N];
        
        for (int i = 0; i < M; i++) {
            String[] line = sc.nextLine().split(" ");
            for (int j = 0; j < N; j++) {
                grid[i][j] = line[j].charAt(0);
            }
        }
        
        int maxLoop = findMaxLoop(grid, M, N);
        System.out.println(maxLoop);
        sc.close();
    }
    
    static int findMaxLoop(char[][] grid, int M, int N) {
        int maxSize = 0;
        
        // Try starting from each cell with each direction
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                for (int dir = 0; dir < 4; dir++) {
                    int loopSize = simulateLight(grid, M, N, i, j, dir);
                    maxSize = Math.max(maxSize, loopSize);
                }
            }
        }
        
        return maxSize;
    }
    
    static int simulateLight(char[][] grid, int M, int N, int startRow, int startCol, int startDir) {
        Set<State> visited = new HashSet<>();
        Set<String> cellsVisited = new HashSet<>();
        
        int row = startRow, col = startCol, dir = startDir;
        
        while (true) {
            // Check if we're out of bounds
            if (row < 0 || row >= M || col < 0 || col >= N) {
                return 0; // No loop, light exits grid
            }
            
            State currentState = new State(row, col, dir);
            
            // Check if we've been in this state before (found a loop)
            if (visited.contains(currentState)) {
                return cellsVisited.size();
            }
            
            visited.add(currentState);
            cellsVisited.add(row + "," + col);
            
            char cell = grid[row][col];
            
            if (cell == '/') {
                // Reflect based on direction
                if (dir == 0) dir = 3;      // Right -> Up
                else if (dir == 1) dir = 2; // Down -> Left
                else if (dir == 2) dir = 1; // Left -> Down
                else if (dir == 3) dir = 0; // Up -> Right
            } else if (cell == '\\') {
                // Reflect based on direction
                if (dir == 0) dir = 1;      // Right -> Down
                else if (dir == 1) dir = 0; // Down -> Right
                else if (dir == 2) dir = 3; // Left -> Up
                else if (dir == 3) dir = 2; // Up -> Left
            }
            // If cell == '0', direction remains unchanged
            
            // Move to next position
            row += dr[dir];
            col += dc[dir];
            
            // Safety check to avoid infinite loops in implementation
            if (visited.size() > M * N * 4) {
                return 0;
            }
        }
    }
}