// Problem Description
// Question -: A positive integer d is said to be a factor of another positive integer N if when N is divided by d, the remainder obtained is zero. For example, for number 12, there are 6 factors 1, 2, 3, 4, 6, 12. Every positive integer k has at least two factors, 1 and the number k itself.Given two positive integers N and k, write a program to print the kth largest factor of N.

// Input Format: The input is a comma-separated list of positive integer pairs (N, k).

// Output Format: The kth highest factor of N. If N does not have k factors, the output should be 1.

// Constraints:

// 1<N<10000000000
// 1<k<600.
// You can assume that N will have no prime factors which are larger than 13.

// Example 1

// Input: 12,3
// Output: 4
// Explanation: N is 12, k is 3. The factors of 12 are (1,2,3,4,6,12). The highest factor is 12 and the third largest factor is 4. The output must be 4.

// Example 2

// Input: 30,9
// Output: 1
// Explanation: N is 30, k is 9. The factors of 30 are (1,2,3,5,6,10,15,30). There are only 8 factors. As k is more than the number of factors, the output is 1.

// Reference: https://prepinsta.com/tcs-codevita/c-program-for-kth-largest-factor-of-n/

import java.util.*;
public class KthLargest{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int k=sc.nextInt();
        System.out.println(findFactors(n,k));
        sc.close();
    }
    private static int findFactors(int num,int k){
        List<Integer> factors=new ArrayList<>();
        for(int i=1;i<num/2;i++){
            if(num%i==0) factors.add(i);
        }
        if(k>factors.size()) return 1;
        return factors.get(factors.size()-k+1);
    }
}