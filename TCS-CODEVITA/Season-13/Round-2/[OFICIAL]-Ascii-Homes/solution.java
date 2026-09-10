
import java.util.*;
import java.io.*;

public class Main {
    static class House {
        int length;
        int height;
        char direction;
        int totalHeight;
        int width;
        char[][] grid;

        public House(int length, int height, char direction) {
            this.length = length;
            this.height = height;
            this.direction = direction;
            calculateDimensions();
            render();
        }

        private void calculateDimensions() {
            int roofHeight = length / 2;
            switch (direction) {
                case 'H':
                    totalHeight = roofHeight + height; // Roof + Walls (H-1) + Base (1) -> L/2 + H
                    width = length + 2; // Base is wider
                    break;
                case 'U':
                    totalHeight = length + height - 1; // Roof(L/2-1) + Base(1) + Walls(H-1) + InvRoof(L/2)
                    width = length;
                    break;
                case 'D':
                    totalHeight = height + roofHeight; // Base(1) + Walls(H-1) + InvRoof(L/2) -> H + L/2
                    width = length;
                    break;
                case 'L':
                    totalHeight = roofHeight + height; // Roof + Base + Walls + Base? Matches H height.
                    width = length + 2;
                    break;
                case 'R':
                    totalHeight = 2 * height + roofHeight; // Roof + Walls + Roof + Walls?
                    width = length;
                    break;
            }
        }

        private void render() {
            grid = new char[totalHeight][width];
            for (char[] row : grid) Arrays.fill(row, ' ');

            int roofHeight = length / 2;
            int wallHeight = height - 1; // Standard wall height

            switch (direction) {
                case 'H':
                    drawRoof(0, roofHeight, false);
                    drawWalls(roofHeight, wallHeight);
                    drawBase(roofHeight + wallHeight, length + 2);
                    break;
                case 'U':
                    drawRoof(0, roofHeight - 1, false); // Top part of roof
                    drawBase(roofHeight - 1, length);
                    drawWalls(roofHeight, wallHeight);
                    drawInvRoof(roofHeight + wallHeight, roofHeight);
                    break;
                case 'D':
                    drawBase(0, length); // Base at top? Or width 2?
                    // Example 2 2x6D has base ## (width 2). L=2. So width L.
                    drawWalls(1, wallHeight);
                    drawInvRoof(1 + wallHeight, roofHeight);
                    break;
                case 'L':
                    // Roof, Base, Walls, Base
                    drawRoof(0, roofHeight, false);
                    drawBase(roofHeight, length); // Inner base
                    drawWalls(roofHeight + 1, wallHeight - 1); // Shortened walls?
                    drawBase(roofHeight + wallHeight, length + 2); // Bottom base
                    break;
                case 'R':
                    // Roof, Walls, Roof, Walls
                    drawRoof(0, roofHeight, false);
                    drawWalls(roofHeight, wallHeight);
                    drawRoof(roofHeight + wallHeight, roofHeight, false);
                    drawWalls(roofHeight + wallHeight + roofHeight, wallHeight);
                    break;
            }
        }

        private void drawRoof(int startRow, int h, boolean inverted) {
            // Standard roof: /\
            // Width starts at 2, increases by 2.
            // Centered in 'length' width?
            // For H, width is length+2. Roof is width length. Centered?
            // 12x8H: Base 16. Roof base 12. Offset 2.
            int centerOffset = (width - length) / 2;
            
            for (int i = 0; i < h; i++) {
                int row = startRow + i;
                if (row >= totalHeight) break;
                int innerSpace = 2 * i;
                int outerSpace = (length - 2 - innerSpace) / 2;
                
                // Left slash
                int leftCol = centerOffset + outerSpace;
                grid[row][leftCol] = '/';
                
                // Right slash
                int rightCol = leftCol + 1 + innerSpace;
                grid[row][rightCol] = '\\';
            }
        }

        private void drawInvRoof(int startRow, int h) {
            // Inverted roof: \/
            // Width starts at length, decreases by 2.
            int centerOffset = (width - length) / 2;
            
            for (int i = 0; i < h; i++) {
                int row = startRow + i;
                if (row >= totalHeight) break;
                int innerSpace = length - 2 - 2 * i;
                int outerSpace = i;
                
                // Left slash
                int leftCol = centerOffset + outerSpace;
                grid[row][leftCol] = '\\';
                
                // Right slash
                int rightCol = leftCol + 1 + innerSpace;
                grid[row][rightCol] = '/';
            }
        }

        private void drawWalls(int startRow, int h) {
            int centerOffset = (width - length) / 2;
            for (int i = 0; i < h; i++) {
                int row = startRow + i;
                if (row >= totalHeight) break;
                grid[row][centerOffset] = '@';
                grid[row][centerOffset + length - 1] = '&';
            }
        }

        private void drawBase(int row, int w) {
            if (row >= totalHeight) return;
            int startCol = (width - w) / 2;
            for (int i = 0; i < w; i++) {
                grid[row][startCol + i] = '#';
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        
        String[] parts = line.trim().split("\\s+");
        List<House> houses = new ArrayList<>();
        int maxTotalHeight = 0;

        for (String part : parts) {
            char dir = part.charAt(part.length() - 1);
            String dims = part.substring(0, part.length() - 1);
            String[] dimParts = dims.split("x");
            int len = Integer.parseInt(dimParts[0]);
            int h = Integer.parseInt(dimParts[1]);
            
            House house = new House(len, h, dir);
            houses.add(house);
            maxTotalHeight = Math.max(maxTotalHeight, house.totalHeight);
        }

        // Render to canvas
        // Bottom aligned
        List<String> outputLines = new ArrayList<>();
        for (int i = 0; i < maxTotalHeight; i++) {
            StringBuilder sb = new StringBuilder();
            for (House house : houses) {
                int startRow = maxTotalHeight - house.totalHeight;
                int houseRow = i - startRow;
                
                if (houseRow >= 0 && houseRow < house.totalHeight) {
                    sb.append(new String(house.grid[houseRow]));
                } else {
                    // Padding
                    for (int k = 0; k < house.width; k++) sb.append(" ");
                }
                // Add spacing between houses? "side by side without any gaps"
                // But Example 1 shows spaces.
                // "aligned neatly side by side along a common base level"
                // "appearing seamlessly side by side without any gaps between the houses"
                // This implies no extra spaces.
                // But the houses themselves have spaces.
                // Let's assume no extra separator.
                sb.append(" "); // Add 1 space for safety? Or 0?
                // Example 1: 6x3U (width 6) 4x2U (width 4).
                // Output: /\ ... / \
                // There is a space between them.
                // Let's add 1 space.
            }
            outputLines.add(sb.toString());
        }

        // Trim trailing spaces
        for (String s : outputLines) {
            System.out.println(s.replaceFirst("\\s++$", ""));
        }
    }
}
