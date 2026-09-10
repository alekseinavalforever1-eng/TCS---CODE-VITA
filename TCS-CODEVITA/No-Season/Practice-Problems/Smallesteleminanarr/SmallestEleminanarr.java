import java.util.Arrays;

public class SmallestEleminanarr{
    public static int findSmallestElement(int[] arr){
        Arrays.sort(arr);
        return arr[0];
    }

    public static void main(String[] args){
        int[] arr1={6,4,2,1,0};
        System.out.println("Smallest element in the array: "+findSmallestElement(arr1));
    }
}

