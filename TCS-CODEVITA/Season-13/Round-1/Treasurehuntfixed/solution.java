import java.util.*;

public class TreasureHuntFixed {
    static int N, M, K;
    static char[][] grid;
    static int startX, startY;
    static Map<Character, Integer> valMap = new HashMap<>();
    static int maxTreasure = 0;

    static int[] dx = {0, 0, -1}; // left, right, up
    static int[] dy = {-1, 1, 0};

    static class State {
        int x, y, stepsLeft, collected;
        State(int x, int y, int stepsLeft, int collected){
            this.x = x;
            this.y = y;
            this.stepsLeft = stepsLeft;
            this.collected = collected;
        }
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        sc.nextLine();

        grid = new char[N][M];
        for(int i=0;i<N;i++){
            String[] row = sc.nextLine().split(" ");
            for(int j=0;j<M;j++) grid[i][j] = row[j].charAt(0);
        }

        startX = sc.nextInt();
        startY = sc.nextInt();
        sc.nextLine();

        int pearl = sc.nextInt();
        int platinum = sc.nextInt();
        int gold = sc.nextInt();
        int diamond = sc.nextInt();
        sc.nextLine();

        K = sc.nextInt();

        valMap.put('$', pearl);
        valMap.put('*', platinum);
        valMap.put('%', gold);
        valMap.put('+', diamond);

        bfs();

        System.out.println(maxTreasure);
        sc.close();
    }

    static void bfs(){
        Queue<State> q = new LinkedList<>();
        int[][][] memo = new int[N][M][K+1];
        for(int i=0;i<N;i++)
            for(int j=0;j<M;j++)
                Arrays.fill(memo[i][j], -1);

        State start = new State(startX, startY, K, valMap.getOrDefault(grid[startX][startY],0));
        start = slide(start);
        q.add(start);
        memo[start.x][start.y][start.stepsLeft] = start.collected;
        maxTreasure = start.collected;

        while(!q.isEmpty()){
            State cur = q.poll();
            for(int d=0;d<3;d++){
                int nx = cur.x + dx[d];
                int ny = cur.y + dy[d];
                if(nx>=0 && nx<N && ny>=0 && ny<M && grid[nx][ny]!='#'){
                    int stepsLeft = cur.stepsLeft - 1;
                    if(stepsLeft<0) continue;
                    int treasure = valMap.getOrDefault(grid[nx][ny],0);
                    State next = new State(nx, ny, stepsLeft, cur.collected + treasure);
                    next = slide(next);
                    if(next.x==N-1) continue; // cannot end in last row
                    if(memo[next.x][next.y][next.stepsLeft]>=next.collected) continue;
                    memo[next.x][next.y][next.stepsLeft] = next.collected;
                    maxTreasure = Math.max(maxTreasure, next.collected);
                    q.add(next);
                }
            }
        }
    }

    static State slide(State s){
        int nx = s.x;
        int collected = s.collected;
        while(nx+1<N && grid[nx+1][s.y]!='#'){
            nx++;
            collected += valMap.getOrDefault(grid[nx][s.y],0);
        }
        return new State(nx, s.y, s.stepsLeft, collected);
    }
}