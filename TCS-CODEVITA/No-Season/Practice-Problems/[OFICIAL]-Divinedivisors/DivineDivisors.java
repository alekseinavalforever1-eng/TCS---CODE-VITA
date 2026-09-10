// ## Problem Description
// Question -: Print a line containing all the divisors in increasing order separated by space.

// Input Format: The first line of input contains an integer ‘N’ denoting the number.

// Output Format: Print a line containing all the divisors in increasing order separated by space.

// Constraints:
// 1 <= N <= 10^8

// S.no	Input	Output	 
// 1	    10	    1 2 5 10

// ## Algorithm Analysis

// - Naive Approach
//     - Time Complexity: O(N)
//     - Space Complexity: O(1)

// - Better Approach
//     - Time Complexity: O(N/2) approx. to O(N)
//     - Space Complexity: O(1)

import java.util.*;
public class DivineDivisors{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int num=sc.nextInt();
        printFactor(num);
        sc.close();
    }
    private static void printFactor(int num){
        for(int i=1;i<=num;i++){
            if(num%i==0) System.out.print(i+" ");
        }
    }
}