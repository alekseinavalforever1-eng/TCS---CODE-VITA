import java.util.*;
public class ConstellationProblem {
    static Map<String, Character>vowelMap = new HashMap<>();
    static {
        vowelMap.put("*.*"+"*.*"+"***",'U');
        vowelMap.put("***"+"*.*"+"***", 'O');
        vowelMap.put("***"+".*."+"***", 'I');
        vowelMap.put("***"+"*.*"+"*.*", 'A');
        vowelMap.put("***"+"***"+"***", 'E');
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        char[][] grid = new char[3][n];
        for(int i=0;i<3;i++){
            String line = sc.nextLine().replace(" ","");
            grid[i]=line.toCharArray();
        }
        StringBuilder result = new StringBuilder();
        for(int col=0;col<n;){
            if(grid[0][col]=='#'){
                result.append('#');
                col++;continue;
            }
            StringBuilder block=new StringBuilder();
            for(int r=0;r<3;r++){
                for(int c=col;c<col+3;c++){
                    block.append(grid[r][c]);
                }
            }
            char vowel=vowelMap.get(block.toString());
            result.append(vowel);
            col+=3;
        }
        System.out.println(result.toString());
        sc.close();
    }
}

