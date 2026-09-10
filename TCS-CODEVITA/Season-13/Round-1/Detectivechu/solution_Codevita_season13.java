import java.util.*;

public class DetectiveChu {
    static int[] dx={-1,0,1,0};
    static int[] dy={0,1,0,-1};
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int R = sc.nextInt();
        int C = sc.nextInt();
        sc.nextLine();
        char[][] grid = new char[R][C];
        for(int i=0; i<R; i++)
        {
            grid[i] = sc.nextLine().toCharArray();
        }
        String seq = sc.nextLine().trim();
        Set<String> result = new HashSet<>();
        for(int i=0; i<R; i++)
        {
            for(int j=0; j<C; j++)
            {
                if(grid[i][j] == '.')
                {
                    for(int dir=0; dir<4; dir++)
                    {
                        int x=i, y=j, d=dir;
                        boolean possible = true;
                        for(int k=seq.length()-1; k>=0; k--)
                        {
                            char move = seq.charAt(k);
                            if (move == 'S')
                            {
                                x -= dx[d];
                                y -= dy[d];
                                if (x<0 || y<0 || x>=R || y>=C || grid[x][y]=='#')
                                {
                                    possible = false;
                                    break;
                                }
                            }
                            else if (move == 'L')
                            {
                                d=(d+1)%4;
                            }
                            else if (move == 'R')
                            {
                                d=(d+3)% 4;
                            }
                        }
                        if (possible)
                        {
                            result.add(i+ "," +j);
                            break;
                        }
                    }
                }
            }
        }

        if (result.isEmpty())
        {
            System.out.print("Impossible");
        }
        else
        {
            System.out.print(result.size());
        }
        sc.close();
    }
}
