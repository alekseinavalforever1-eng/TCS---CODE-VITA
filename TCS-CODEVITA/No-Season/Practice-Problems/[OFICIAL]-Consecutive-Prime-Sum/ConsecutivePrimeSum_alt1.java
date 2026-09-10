import java.util.*;
public class ConsecutivePrimeSum 
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();

        boolean[] isPrime = new boolean[n+1];
        Arrays.fill(isPrime, true);
        isPrime[0]=isPrime[1]=false;
        for(int i=2;i*i<=n;i++){
            if(isPrime[i]){
                for(int j=i*i;j<=n;j+=i){
                    isPrime[j]=false;
                }
            }
        }
        List<Integer> primes = new ArrayList<>();
        for(int i=2;i<=n;i++){
            if(isPrime[i]){
            primes.add(i);
            }
        }
        int count=0;
        int sum=0;
        for(int i=0;i<primes.size();i++){
            sum+=primes.get(i);
            if(sum>n)break;
            if(isPrime[sum]){
                count++;
            }
        }
        System.out.println(count);
        sc.close();
    }
}
