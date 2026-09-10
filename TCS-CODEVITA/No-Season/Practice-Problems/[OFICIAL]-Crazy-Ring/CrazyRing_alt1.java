// Scientists have found a strange substance having strange properties. There is one triangular substance called Strange Triangle which has a property that if it is placed inside a circle then it expands until all the corners of the triangle are touching the circle. There is another circular substance called Strange Circle, which when placed inside any polygon, expands such that it becomes the largest possible circle which can fit inside the polygon such that it touches every side of the polygon.


// Now researchers did a strange experiment. They placed a Strange Triangle inside a normal circle and then placed a Strange Circle inside this Strange Triangle. Thus the ring formed by the two circles, the normal outer circle and the inner strange circle is named Crazy Ring. You are provided with the coordinates of the Strange Triangle on coordinate plane and you have to calculate the area of the Crazy Ringformed by the structure, Print "Not Possible" if the ring is not possible to form.

// Input Format:
// First line contains two space delimited numbers N1 M1 (N1 and M1 can also be negative)
// Second line contains two space delimited numbers N2 M2 (N2 and M2 can also be negative)
// Third line contains two space delimited numbers N3 M3 (N3 and M3 can also be negative)
// Where, (N1, M1) , (N2, M2) and (N3, M3) are x and y coordinates of three points representing the Strange Triangle

// Output Format:

// Output the area of the crazy ring up to 2 decimal places however calculations are to be performed up to a precision of 11 decimal places

// OR

// Print "Not Possible" if it is not possible to form the ring
// Sample Input and Output

// Testcases:

// ```
// 5 5
// 5 20
// 20 5 

// Ans
// 292.79 
// ```

// ```
// 5 5
// 5 5
// 5 5 	

// Ans
// Not Possible
// ```

// ```
// 5 8
// 4 3
// 2 4.34534554521 	

// Ans
// 17.91
// ```
import java.util.*;
public class CrazyRing{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        Double x1=sc.nextDouble();
        Double y1=sc.nextDouble();
        Double x2=sc.nextDouble();
        Double y2=sc.nextDouble();
        Double x3=sc.nextDouble();
        Double y3=sc.nextDouble();
        if(findTriangleArea(x1,y1,x2,y2,x3,y3)==0){
            System.out.println("Not Possible");
        }else{
            Double res=findAreaRing(x1,y1,x2,y2,x3,y3);
            System.out.printf("%.2f",res);
        }
        sc.close();
    }
    
    public static Double findTriangleArea(Double x1, Double y1, Double x2, Double y2, Double x3, Double y3) {
        Double area = Math.abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0;
        return area;
    }
    
    public static Double findAreaRing(Double x1, Double y1, Double x2, Double y2, Double x3, Double y3) {
        Double triangleArea = findTriangleArea(x1, y1, x2, y2, x3, y3);
        
        Double a = Math.sqrt(Math.pow(x2 - x3, 2) + Math.pow(y2 - y3, 2));
        Double b = Math.sqrt(Math.pow(x1 - x3, 2) + Math.pow(y1 - y3, 2));
        Double c = Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
        
        Double circumradius = (a * b * c) / (4 * triangleArea);
        Double semiPerimeter = (a + b + c) / 2.0;
        Double inradius = triangleArea / semiPerimeter;
        
        Double ringArea = Math.PI * (circumradius * circumradius - inradius * inradius);
        return ringArea;
    }
}