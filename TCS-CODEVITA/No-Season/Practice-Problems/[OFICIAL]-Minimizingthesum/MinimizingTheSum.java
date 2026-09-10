// Problem Description
// Given an array of integers, perform atmost K operations so that the sum of elements of final array is minimum. An operation is defined as follows –

// Consider any 1 element from the array, arr[i].
// Replace arr[i] by floor(arr[i]/2).
// Perform next operations on the updated array.
// The task is to minimize the sum after utmost K operations.
// Constraints

// 1 <= N
// K <= 10^5.
// Input

// First line contains two integers N and K representing size of array and maximum numbers of operations that can be performed on the array respectively.
// Second line contains N space separated integers denoting the elements of the array, arr.
// Output

// Print a single integer denoting the minimum sum of the final array.
// Input

// 4 3

// 20 7 5 4

// Output

// 17

// Explanation

// Operation 1 -> Select 20. Replace it by 10. New array = [10, 7, 5, 4]
// Operation 2 -> Select 10. Replace it by 5. New array = [5, 7, 5, 4].
// Operation 3 -> Select 7. Replace it by 3. New array = [5,3,5,4].
// Sum = 17.
import java.util.*;

public class MinimizingTheSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        int[] numbers = new int[n];

        for (int i=0;i<n;i++) numbers[i] = sc.nextInt();

        System.out.println(minimize(numbers, n, k));

        sc.close();
    }

    private static int minimize(int[] numbers, int n, int k) { 
        int minSum = 9999999;

        while (k-- > 0) {
            int[] res = findMaximum(numbers);
            int maxIndex = res[1];

            numbers[maxIndex] = (int) Math.floor(numbers[maxIndex]/2.0);
            int curSum = findSum(numbers);

            minSum = Math.min(minSum, curSum);
        }

        return minSum;
    }

    private static int[] findMaximum(int[] arr) {
        int[] res = new int[2];

        for (int i=0;i<arr.length;i++) {
            if (arr[i] > res[0]) {
                res[0] = arr[i];
                res[1] = i;
            }
        }

        return res;
    }

    private static int findSum(int[] arr) {
        int sum = 0;

        for (int i=0;i<arr.length;i++) sum += arr[i];

        return sum;
    }
}
