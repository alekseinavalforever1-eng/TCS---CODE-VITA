import java.util.*;

public class ArrangeTrack {
    static int N, M;
    static char[][] originalGrid;
    static int sheetCount;
    static Sheet[][] sheets;
    static int minDistance = Integer.MAX_VALUE;
    static int sx, sy, dx, dy;

    static int[] dirX = {-1,1,0,0};
    static int[] dirY = {0,0,-1,1};

    static class Sheet {
        char[][] data;
        int size;
        public Sheet(char[][] d){
            size = d.length;
            data = new char[size][size];
            for(int i=0;i<size;i++)
                System.arraycopy(d[i],0,data[i],0,size);
        }
        // Rotate 90 degrees clockwise
        public Sheet rotate(){
            char[][] r = new char[size][size];
            for(int i=0;i<size;i++)
                for(int j=0;j<size;j++)
                    r[j][size-1-i] = data[i][j];
            return new Sheet(r);
        }
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        sc.nextLine();
        originalGrid = new char[N][N];
        for(int i=0;i<N;i++){
            String line = sc.nextLine();
            for(int j=0;j<N;j++){
                originalGrid[i][j] = line.charAt(j);
                if(originalGrid[i][j]=='S'){ sx=i; sy=j; }
                if(originalGrid[i][j]=='D'){ dx=i; dy=j; }
            }
        }

        sheetCount = N / M;
        sheets = new Sheet[sheetCount][sheetCount];
        for(int i=0;i<sheetCount;i++){
            for(int j=0;j<sheetCount;j++){
                char[][] s = new char[M][M];
                for(int x=0;x<M;x++)
                    for(int y=0;y<M;y++)
                        s[x][y] = originalGrid[i*M+x][j*M+y];
                sheets[i][j] = new Sheet(s);
            }
        }

        Sheet[][] arrangement = new Sheet[sheetCount][sheetCount];
        arrangeSheets(0,0,arrangement);
        System.out.println(minDistance);
        sc.close();
    }

    static void arrangeSheets(int r, int c, Sheet[][] arrangement){
        if(r==sheetCount){
            char[][] fullGrid = mergeSheets(arrangement);
            int dist = bfs(fullGrid);
            if(dist!=-1) minDistance = Math.min(minDistance, dist);
            return;
        }

        int nextR = (c==sheetCount-1)? r+1 : r;
        int nextC = (c==sheetCount-1)? 0 : c+1;

        Sheet current = sheets[r][c];

        // S sheet (top-left) and D sheet (bottom-right) fixed
        if((r==0 && c==0) || (r==sheetCount-1 && c==sheetCount-1)){
            arrangement[r][c] = current;
            arrangeSheets(nextR,nextC,arrangement);
        } else {
            Sheet rotated = current;
            for(int i=0;i<4;i++){
                if(canPlace(rotated,r,c,arrangement)){
                    arrangement[r][c] = rotated;
                    arrangeSheets(nextR,nextC,arrangement);
                }
                rotated = rotated.rotate();
            }
        }
    }

    static boolean canPlace(Sheet s, int r, int c, Sheet[][] arrangement){
        if(r>0){
            Sheet top = arrangement[r-1][c];
            for(int i=0;i<M;i++){
                if((top.data[M-1][i]=='T') != (s.data[0][i]=='T')) return false;
            }
        }
        if(c>0){
            Sheet left = arrangement[r][c-1];
            for(int i=0;i<M;i++){
                if((left.data[i][M-1]=='T') != (s.data[i][0]=='T')) return false;
            }
        }
        return true;
    }

    static char[][] mergeSheets(Sheet[][] arrangement){
        char[][] full = new char[N][N];
        for(int i=0;i<sheetCount;i++){
            for(int j=0;j<sheetCount;j++){
                Sheet s = arrangement[i][j];
                for(int x=0;x<M;x++)
                    for(int y=0;y<M;y++)
                        full[i*M+x][j*M+y] = s.data[x][y];
            }
        }
        return full;
    }

    static int bfs(char[][] grid){
        boolean[][] visited = new boolean[N][N];
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{sx,sy,1});
        visited[sx][sy]=true;

        while(!q.isEmpty()){
            int[] cur = q.poll();
            int x=cur[0], y=cur[1], d=cur[2];
            if(x==dx && y==dy) return d;
            for(int k=0;k<4;k++){
                int nx=x+dirX[k], ny=y+dirY[k];
                if(nx>=0 && ny>=0 && nx<N && ny<N && !visited[nx][ny] && (grid[nx][ny]=='T'||grid[nx][ny]=='D')){
                    visited[nx][ny]=true;
                    q.add(new int[]{nx,ny,d+1});
                }
            }
        }
        return -1;
    }
}
