// Question - Christmas Tower
// 	Daiwik received an exciting Christmas present from his Secret Santa. The present consists of multiple
// repeated blocks, each varying in size. There are five unique blocks, all with identical width but varying
// heights. Daiwik's task is to construct a tower using these blocks, ensuring he uses the maximum number of
// blocks and the overall height does not surpass a specified height H.
// Given that Daiwik has an infinite supply of each block type, print the block heights prioritizing the
// frequencies in descending order, at which they were utilized in constructing the tower. If one or more type
// of blocks are used with same frequency, then print them in the ascending order of their heights.
// Constraints
// 1 <= L <= 10^4
// 1 <= heights of five blocks <= 10^3
// Input
// First line consists of L denoting the height of the tower that Daiwik is going to build.
// Next line consists of five space separated integers denoting the heights of the blocks that Daiwik have.
// Output
// Print the block heights in descending order based on their frequency of usage in constructing the tower,
// separated by space. If one or more type of blocks are used with same frequency, then print them in the
// ascending order of their heights. Print "Impossible" if its not possible to construct a tower of height H.
// Time Limit (secs)
// 1
// Examples
// Example 1
// Input
// 13
// 2 7 3 4 9
// Output
// 2 3
// Explanation
// To construct a tower with a height of 13, utilizing blocks of sizes {2, 7, 3, 4, 9}, Daiwik can opt for five blocks
// with a height 2 and a single block with a height of 3. This configuration would yield a total height of 2 * 5 +
// 3 * 1 = 13.
// Example 2
// Input
// 19
// 2 4 6 8 10
// Output
// Impossible
// Explanation
// Constructing a tower of height 19 using the provided combination of blocks is not feasible. Hence, print
// "Impossible".
// =======
// Question - Christmas Tower
// 	Daiwik received an exciting Christmas present from his Secret Santa. The present consists of multiple
// repeated blocks, each varying in size. There are five unique blocks, all with identical width but varying
// heights. Daiwik's task is to construct a tower using these blocks, ensuring he uses the maximum number of
// blocks and the overall height does not surpass a specified height H.
// Given that Daiwik has an infinite supply of each block type, print the block heights prioritizing the
// frequencies in descending order, at which they were utilized in constructing the tower. If one or more type
// of blocks are used with same frequency, then print them in the ascending order of their heights.
// Constraints
// 1 <= L <= 10^4
// 1 <= heights of five blocks <= 10^3
// Input
// First line consists of L denoting the height of the tower that Daiwik is going to build.
// Next line consists of five space separated integers denoting the heights of the blocks that Daiwik have.
// Output
// Print the block heights in descending order based on their frequency of usage in constructing the tower,
// separated by space. If one or more type of blocks are used with same frequency, then print them in the
// ascending order of their heights. Print "Impossible" if its not possible to construct a tower of height H.
// Time Limit (secs)
// 1
// Examples
// Example 1
// Input
// 13
// 2 7 3 4 9
// Output
// 2 3
// Explanation
// To construct a tower with a height of 13, utilizing blocks of sizes {2, 7, 3, 4, 9}, Daiwik can opt for five blocks
// with a height 2 and a single block with a height of 3. This configuration would yield a total height of 2 * 5 +
// 3 * 1 = 13.
// Example 2
// Input
// 19
// 2 4 6 8 10
// Output
// Impossible
// Explanation
// Constructing a tower of height 19 using the provided combination of blocks is not feasible. Hence, print
// "Impossible".

import java.util.*;
public class ChristmasTower {
    public static void christmasTower(int[] a,int n, int mx){
        for(int idx=1;idx<n;idx++){
            if(a[idx-1]>a[idx]){
                int t=a[idx-1];
                a[idx-1]=a[idx];
                a[idx]=t;
            }
            Map<Integer,Integer> fq=new HashMap<>();
            int[] tw=new int[10001];
            Arrays.fill(tw,-1);
            tw[0]=0;
            for(int block:a)
                for(int j=block;j<=mx;j++)
                    if(tw[j-block]!=-1)
                        tw[j]=Math.max(tw[j],tw[j-block]+1);
            if(tw[mx]==-1){
                System.out.println("Impossible");
                return;
            }
            int k=mx;
            while(k>0){
                for(int block:a)
                    if(k-block>=0 && tw[k]==tw[k-block]+1){
                        fq.put(block,fq.getOrDefault(block,0)+1);
                        k-=block;
                        break;
                    }
            }
            List<Map.Entry<Integer,Integer>> res=new ArrayList<>(fq.entrySet());
            int sz=res.size(),c=0;
            res.sort(Comparator.comparing(Map.Entry<Integer,Integer>::getValue).reversed()
                    .thenComparing(Map.Entry<Integer,Integer>::getKey));
            for(Map.Entry<Integer,Integer> entry:res){
                c++;
                if(c<sz)
                    System.out.print(entry.getKey()+" ");
                else
                    System.out.print(entry.getKey());
            }
        }
    }
    public static void main(String[] args){
        Scanner x=new Scanner(System.in);
        int mx=x.nextInt();
        int[] a=new int[5];
        for(int i=0;i<5;i++)
            a[i]=x.nextInt();
        christmasTower(a,5,mx);
        x.close();
    }
    
}