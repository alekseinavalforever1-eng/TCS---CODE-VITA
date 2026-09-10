import java.util.*;
import java.io.*;

class Main {

    static class Point {
        double x, y;

        public Point(double x, double y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Point point = (Point) o;
            // Use a small epsilon for floating-point comparison
            return Math.abs(x - point.x) < 1e-9 && Math.abs(y - point.y) < 1e-9;
        }

        @Override
        public int hashCode() {
            return Objects.hash((int) (x * 1000), (int) (y * 1000));
        }
    }

    static class Line {
        Point p1, p2;

        public Line(int x1, int y1, int x2, int y2) {
            if (x1 > x2 || (x1 == x2 && y1 > y2)) {
                this.p1 = new Point(x2, y2);
                this.p2 = new Point(x1, y1);
            } else {
                this.p1 = new Point(x1, y1);
                this.p2 = new Point(x2, y2);
            }
        }
        
        // Helper to check if a point lies on the line segment
        public boolean isPointOnSegment(Point p) {
            double crossProduct = (p.y - p1.y) * (p2.x - p1.x) - (p.x - p1.x) * (p2.y - p1.y);
            if (Math.abs(crossProduct) > 1e-9) return false;

            double dotProduct = (p.x - p1.x) * (p2.x - p1.x) + (p.y - p1.y) * (p2.y - p1.y);
            if (dotProduct < 0) return false;

            double squaredLength = (p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y);
            if (dotProduct > squaredLength) return false;

            return true;
        }

        // Get slope
        public double getSlope() {
            if (p1.x == p2.x) return Double.POSITIVE_INFINITY; // Vertical line
            return (p2.y - p1.y) / (p2.x - p1.x);
        }
    }

    // Function to calculate intersection point of two lines
    public static Point getIntersection(Line l1, Line l2) {
        double x1 = l1.p1.x, y1 = l1.p1.y, x2 = l1.p2.x, y2 = l1.p2.y;
        double x3 = l2.p1.x, y3 = l2.p1.y, x4 = l2.p2.x, y4 = l2.p2.y;

        double denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);
        if (Math.abs(denominator) < 1e-9) {
            return null; // Parallel or collinear
        }

        double t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator;
        double u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator;

        if (t >= -1e-9 && t <= 1 + 1e-9 && u >= -1e-9 && u <= 1 + 1e-9) {
            // Intersection point
            double x = x1 + t * (x2 - x1);
            double y = y1 + t * (y2 - y1);
            return new Point(x, y);
        }
        return null;
    }

    // Function to calculate number of cells touched
    public static int numCellsTouched(Point p1, Point p2) {
        return (int) Math.max(Math.round(Math.abs(p1.x - p2.x)), Math.round(Math.abs(p1.y - p2.y)));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        Line[] lines = new Line[N];
        for (int i = 0; i < N; i++) {
            int x1 = scanner.nextInt();
            int y1 = scanner.nextInt();
            int x2 = scanner.nextInt();
            int y2 = scanner.nextInt();
            lines[i] = new Line(x1, y1, x2, y2);
        }
        int K = scanner.nextInt();

        Map<Point, Set<Integer>> intersections = new HashMap<>();

        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                Point intersectPoint = getIntersection(lines[i], lines[j]);
                if (intersectPoint != null) {
                    intersections.computeIfAbsent(intersectPoint, k -> new HashSet<>()).add(i);
                    intersections.get(intersectPoint).add(j);
                }
            }
        }

        long totalIntensity = 0;
        for (Map.Entry<Point, Set<Integer>> entry : intersections.entrySet()) {
            Point starPoint = entry.getKey();
            Set<Integer> lineIndices = entry.getValue();

            if (lineIndices.size() == K) {
                int minIntensity = Integer.MAX_VALUE;
                for (int lineIdx : lineIndices) {
                    Line line = lines[lineIdx];
                    
                    if (starPoint.equals(line.p1) || starPoint.equals(line.p2)) {
                        // Case 1: One-sided
                        int cells = numCellsTouched(starPoint, starPoint.equals(line.p1) ? line.p2 : line.p1);
                        minIntensity = Math.min(minIntensity, cells);
                    } else {
                        // Case 2: Two-sided
                        int cells1 = numCellsTouched(starPoint, line.p1);
                        int cells2 = numCellsTouched(starPoint, line.p2);
                        minIntensity = Math.min(minIntensity, cells1);
                        minIntensity = Math.min(minIntensity, cells2);
                    }
                }
                if (minIntensity != Integer.MAX_VALUE) {
                    totalIntensity += minIntensity;
                }
            }
        }

        System.out.println(totalIntensity);
        scanner.close();
    }
}