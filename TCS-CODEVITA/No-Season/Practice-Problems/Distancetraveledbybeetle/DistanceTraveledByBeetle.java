// //Distance Traveled by Beetle
// A 
// 10
// c
// m
// ×
// 10
// c
// m
// ×
// 10
// c
// m
// 10cm×10cm×10cm solid cube rests on the ground. It has a beetle on it, as well as some sweet honey spots on the cube’s surface. The beetle begins at a point on the cube’s surface and moves in a clockwise direction along the cube’s surface to the honey spots.

// If it goes from one point on the same face to another (say, X to Y), it goes in an arc of a circle that subtends an angle of 60 degrees at the circle’s center. If it travels from one point to another on a different face, it takes the shortest path on the cube’s surface, except that it never travels along its bottom. The beetle is a Cartesian geometry student who knows the coordinates (
// x
// ,
// y
// ,
// z
// x,y,z) of all the points it needs to visit. Its coordinate origin is one of the cube’s corners on the ground, and the z-axis points up. As a result, 
// z
// =
// 0
// z=0 is the bottom surface (on which it does not crawl), and 
// z
// =
// 10
// z=10 is the top. The beetle keeps track of all distances traveled and rounded the distance to two decimal places when it arrives at the following location so that the final distance is a sum of the rounded distances from spot to spot.

// Input Format
// The first line returns an integer 
// N
// N, the total number of points visited by the beetle (including the starting point).

// The second line contains 
// 3
// N
// 3N non-negative numbers, each with two decimal places. These are to be interpreted as the x, y, and z coordinates of the points the beetle must visit in the given order.

// Output Format
// One line containing a number representing the total distance traveled by the beetle to two decimal places. Even if the travel distance is an integer, the output should have two decimal places.

// Constraints
// None of the points visited by the beetle are on the bottom face (z=0) or on any of the cube’s edges (the lines where two faces meet)

// 2
// ≤
// N
// ≤
// 10
// 2≤N≤10

// Sample 1:
// Input
// Output
// 3
// 1 1 10 2 1 10 0 1 9
// 4.05
// Explanation:
// The beetle visits three different locations (N=3). The beetle begins on the cube's 
// top face (z=10) at point (1,1,10) and moves to another point on the same face (2,1,10). 
// Although the straight line distance is one, it travels on the arc of a circle with an angle of 60 degrees at its center and thus travels (2*pi)/6 or 1.05 
// (note that it rounds the distance at each leg of the journey). It moves along the cube's surface from (2,1,10) on the face z=10 to (0,1,9) on the face x=0. 
// This is a three-mile distance. The total travel distance is 1.05+3=4.05. The result is 4.05

import java.util.*;
public class DistanceTraveledByBeetle {
    static class Point{
        double x,y,z;
        Point(double a, double b, double c){
            x = a;
            y = b;
            z = c;
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Point[] pts = new Point[N];
        for(int i=0;i<N;i++){
            double x = sc.nextDouble();
            double y = sc.nextDouble();
            double z = sc.nextDouble();
            pts[i] = new Point(x,y,z);
        }
        double total = 0.0;

        for(int i=0;i<N-1;i++){
            double segment= distance(pts[i], pts[i+1]);
            segment=Math.round(segment*100.0)/100.0;
            total += segment;
        }
        System.out.printf("%.2f\n", total);
        sc.close();
    }
    static String face(Point p){
        if(Math.abs(p.z - 10) < 1e-9) return "top";
        if(Math.abs(p.x - 10) < 1e-9) return "right";
        if(Math.abs(p.x - 0) < 1e-9) return "left";
        if(Math.abs(p.y - 10) < 1e-9) return "front";
        if(Math.abs(p.y - 0) < 1e-9) return "back";
        return "Invalid";
    }
    static double distance(Point a, Point b) {
        String fa=face(a);
        String fb=face(b);
        
        if(fa.equals(fb)){
            // Same face arc movement
            double d =sameFaceDistance(a, b,fa);
            return d*(Math.PI/3.0);
        }
        // Different face shortest path
        return unfoldedShortest(a,b);
    }
    //Euclidean distance on same face
    static double sameFaceDistance(Point a, Point b, String face){
        if(face.equals("top")||face.equals("bottom"))
            return Math.hypot(a.x - b.x, a.y - b.y);
        if(face.equals("left")||face.equals("right"))
            return Math.hypot(a.y - b.y, a.z - b.z);
        return Math.hypot(a.x - b.x, a.z - b.z);   
    }
    static double unfoldedShortest(Point a,Point b){
        List<double[]> A=unwrap(a);
        List<double[]> B=unwrap(b);

        double best=Double.MAX_VALUE;
        for(double[] pa:A)
            for(double[] pb:B){
                best=Math.min(best, Math.hypot(pa[0]-pb[0],pa[1]-pb[1]));
            }
        return best;
    }
    static List<double[]> unwrap(Point p){
        List<double[]> list=new ArrayList<>();
        if(Math.abs(p.z-10)<1e-9){
            list.add(new double[]{p.x,p.y}); //top
        }
        if(Math.abs(p.x-10)<1e-9){
            list.add(new double[]{10+p.z,p.y}); //right
        }
        if(Math.abs(p.x-0)<1e-9){
            list.add(new double[]{-p.z,p.y}); //left
        }
        if(Math.abs(p.y-10)<1e-9){
            list.add(new double[]{p.x,10 + p.z}); //front
        }
        if(Math.abs(p.y-0)<1e-9){
            list.add(new double[]{p.x,-10 + p.z}); //back
    }
        return list;
}
}
