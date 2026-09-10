import java.util.*;

public class ReenuCircuit {

    static int N;
    static char[][] grid;
    static int startX, startY, endX, endY;
    static Set<String> visited;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        grid = new char[N][N];
        int terminalCount = 0;

        for (int i = 0; i < N; i++) {
            String row = scanner.next();
            for (int j = 0; j < N; j++) {
                grid[i][j] = row.charAt(j);
                if (grid[i][j] == '.') {
                    if (terminalCount == 0) {
                        startX = i;
                        startY = j;
                    } else {
                        endX = i;
                        endY = j;
                    }
                    terminalCount++;
                }
            }
        }
        scanner.close();

        visited = new HashSet<>();
        double totalResistance = findResistance(startX, startY);
        System.out.printf("%.1f\n", totalResistance);
    }
    
    // Recursive function to calculate the equivalent resistance from (x, y)
    private static double findResistance(int x, int y) {
        String pos = x + "," + y;
        visited.add(pos);

        if (x == endX && y == endY) {
            visited.remove(pos);
            return 0.0;
        }

        List<int[]> neighbors = new ArrayList<>();
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                String neighborPos = nx + "," + ny;
                if (!visited.contains(neighborPos) || (nx == endX && ny == endY)) {
                    // Check if the move is valid based on component type
                    boolean validMove = false;
                    if (grid[x][y] == '+' || grid[x][y] == '.') {
                        validMove = true;
                    } else if (grid[x][y] == '-' && dy[i] != 0) {
                        validMove = true;
                    } else if (grid[x][y] == '|' && dx[i] != 0) {
                        validMove = true;
                    }
                    
                    if (validMove) {
                        // Check if the path is valid from the neighbor's side too
                        if (grid[nx][ny] == '+' || grid[nx][ny] == '.') {
                            neighbors.add(new int[]{nx, ny});
                        } else if (grid[nx][ny] == '-' && dy[i] != 0) {
                            neighbors.add(new int[]{nx, ny});
                        } else if (grid[nx][ny] == '|' && dx[i] != 0) {
                            neighbors.add(new int[]{nx, ny});
                        }
                    }
                }
            }
        }

        double result;
        if (neighbors.size() > 1) {
            // Parallel branches from a junction or terminal
            double inverseSum = 0.0;
            for (int[] neighbor : neighbors) {
                double branchRes = 0.0;
                if (grid[neighbor[0]][neighbor[1]] == '-' || grid[neighbor[0]][neighbor[1]] == '|') {
                    branchRes = 1.0;
                }
                inverseSum += 1.0 / (branchRes + findResistance(neighbor[0], neighbor[1]));
            }
            result = 1.0 / inverseSum;
        } else if (neighbors.size() == 1) {
            // Series connection
            int[] neighbor = neighbors.get(0);
            double resistance = 0.0;
            if (grid[neighbor[0]][neighbor[1]] == '-' || grid[neighbor[0]][neighbor[1]] == '|') {
                resistance = 1.0;
            }
            result = resistance + findResistance(neighbor[0], neighbor[1]);
        } else {
            // Dead end (no valid paths to the destination)
            result = Double.MAX_VALUE / 2;
        }

        visited.remove(pos);
        return result;
    }
}