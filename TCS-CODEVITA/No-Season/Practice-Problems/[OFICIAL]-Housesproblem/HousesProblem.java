// ## Problem Statement

// There are n houses build in a line, each of which contains some value in it.

// A thief is going to steal the maximal value of these houses, but he can’t steal in two adjacent houses because the owner of the stolen houses will tell his two neighbours left and right side.

// What is the maximum stolen value?


// ## Algorithm Analysis

// - Dynamic Programming Approach with Memorization table
//     - Time Complexity: O(N)
//     - Space Complexity: O(N)

// - Space Optimized Dynamic Approach
//     - Time Complexity: O(N)
//     - Space Complexity: O(1)

import java.util.*;
public class HousesProblem{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int houses=sc.nextInt();
        int[] money=new int[houses];
        for(int i=0;i<houses;i++) money[i]=sc.nextInt();
        sc.close();
        System.out.println(robBest(money)); 
    }
    private static int robBest(int[] money){
        if(money.length<2) return money[0];
        int[] memo = new int[money.length];
        memo[0]=money[0];
        memo[1]=Math.max(money[0],money[1]);
        for(int i=2;i<money.length;i++){
            memo[i]=Math.max(memo[i-2],money[i]+memo[i-1]);
        }
        return memo[money.length-1];
    }
       
}