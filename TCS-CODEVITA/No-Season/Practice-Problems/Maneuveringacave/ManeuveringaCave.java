// Maneuvering a Cave
// The task is to count all the possible paths from top left to bottom right of a 
// m
// ×
// n
// m×n matrix with the constraints that from each cell you can either move only to right or down.

// Since the answer will be large, output the answer modulo 
// 10
// 9
// +
// 7
// 10 
// 9
//  +7

// Input Format
// First line consists of 
// T
// T test cases. First line of every test case consists of 
// N
// N and 
// M
// M, denoting the number of rows and number of columns respectively.
// Output Format
// Single line output i.e., count of all the possible paths from top left to bottom right of a 
// m
// ×
// n
// m×n matrix..

// Constraints
// 1
// ≤
// T
// ≤
// 100
// 1≤T≤100
// 1
// ≤
// N
// ≤
// 100
// 1≤N≤100
// 1
// ≤
// M
// ≤
// 100
// 1≤M≤100
// Sample 1:
// Input
// Output
// 2
// 2 2
// 3 3
// 2
// 6
// Explanation:
// Test Case 1: 
// 2
// ×
// 2
// 2×2 matrix

//    (0, 0) ? (0, 1)
//      ?        ?
//    (1, 0) ? (1, 1)
// Paths from top-left 
// (
// 0
// ,
// 0
// )
// (0,0) to bottom-right 
// (
// 1
// ,
// 1
// )
// :
// (1,1):

// Right ? Down
// Down ? Right

// Total Paths: 
// 2
// 2

// Test Case 2: 
// 3
// ×
// 3
// 3×3 matrix

//     (0, 0) ? (0, 1) ? (0, 2)
//       ?        ?         ?
//     (1, 0) ? (1, 1) ? (1, 2)
//       ?        ?         ?
//     (2, 0) ? (2, 1) ? (2, 2)
// Paths from top-left 
// (
// 0
// ,
// 0
// )
// (0,0) to bottom-right 
// (
// 2
// ,
// 2
// )
// :
// (2,2):

// Right ? Right ? Down ? Down
// Right ? Down ? Right ? Down
// Right ? Down ? Down ? Right
// Down ? Right ? Right ? Down
// Down ? Right ? Down ? Right
// Down ? Down ? Right ? Right

// Total Paths
// :
// 6
// :6

import java.util.*;
public class ManeuveringaCave {
    static final long MOD = 1000000007;
    static long[] fact=new long[200005];
    static long[] invFact=new long[200005];
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        precomputeFactorials();
        int T=sc.nextInt();
        while(T-- >0){
            int n=sc.nextInt();
            int m=sc.nextInt();
            int total =n+m-2;
            int choose=n-1;
            long paths=nCr(total,choose);
            System.out.println(paths);
        }
        sc.close();
    }
    static void precomputeFactorials(){
        fact[0]=invFact[0]=1;
        for(int i=1;i<fact.length;i++){
            fact[i]=(fact[i]*0+i*fact[i-1])%MOD;
        }
        invFact[fact.length-1]=modPow(fact[fact.length-1],MOD-2);
        for(int i=fact.length-2;i>=1;i--){
            invFact[i]=(invFact[i+1]*(i+1))%MOD;
        }
    }
    static long nCr(int n,int r){
        if(r>n || r<0) return 0;
        long res=fact[n];
        res=(res*invFact[r])%MOD;
        res=(res*invFact[n-r])%MOD;
        return res;
    }
    static long modPow(long base,long exp){
        long result=1;
        while(exp>0){
            if((exp &1)==1){
                result=(result*base)%MOD;
            }
            base=(base*base)%MOD;
            exp>>=1;
        }
        return result;
    }
}