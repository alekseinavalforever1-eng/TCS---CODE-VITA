import java.util.*;

public class StellarJourney {
    static class Segment {
        int x1, y1, x2, y2;
        Segment(int a, int b, int c, int d){ x1=a; y1=b; x2=c; y2=d; }
    }

    static class Star {
        int id;
        List<Segment> segments = new ArrayList<>();
        Set<String> points = new HashSet<>();
        Star(int id){ this.id=id; }
        void addSegment(Segment s){
            segments.add(s);
            points.add(s.x1+","+s.y1);
            points.add(s.x2+","+s.y2);
        }
    }

    static boolean sharePoint(Star a, Star b){
        for(String p : a.points){
            if(b.points.contains(p)) return true;
        }
        return false;
    }

    static int bfs(boolean[][] graph, int start, int end){
        Queue<int[]> q = new LinkedList<>();
        boolean[] visited = new boolean[graph.length];
        q.add(new int[]{start,1});
        visited[start]=true;
        while(!q.isEmpty()){
            int[] cur = q.poll();
            int node = cur[0], dist = cur[1];
            if(node==end) return dist;
            for(int i=0;i<graph.length;i++){
                if(graph[node][i] && !visited[i]){
                    visited[i]=true;
                    q.add(new int[]{i,dist+1});
                }
            }
        }
        return -1;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Segment[] segs = new Segment[N];
        for(int i=0;i<N;i++){
            int a=sc.nextInt(), b=sc.nextInt(), c=sc.nextInt(), d=sc.nextInt();
            segs[i] = new Segment(a,b,c,d);
        }
        int sx = sc.nextInt(), sy = sc.nextInt();
        int dx = sc.nextInt(), dy = sc.nextInt();

        // Step 1: Group segments into stars (DFS on shared points)
        boolean[] visited = new boolean[N];
        List<Star> stars = new ArrayList<>();
        int starId=0;
        for(int i=0;i<N;i++){
            if(!visited[i]){
                Star s = new Star(starId++);
                dfs(i, segs, visited, s);
                stars.add(s);
            }
        }

        // Step 2: Build connectivity graph
        int nStars = stars.size();
        boolean[][] graph = new boolean[nStars][nStars];
        for(int i=0;i<nStars;i++){
            for(int j=i+1;j<nStars;j++){
                if(sharePoint(stars.get(i), stars.get(j))){
                    graph[i][j]=graph[j][i]=true;
                }
            }
        }

        // Step 3: Identify start and destination stars
        int startStar=-1, endStar=-1;
        for(Star s: stars){
            for(Segment seg: s.segments){
                if(startStar==-1 && pointOnSegment(seg, sx, sy)) startStar = s.id;
                if(endStar==-1 && pointOnSegment(seg, dx, dy)) endStar = s.id;
            }
        }

        if(startStar==-1 || endStar==-1){
            System.out.println("Impossible");
            return;
        }

        // Step 4: BFS to find minimum stars
        int ans = bfs(graph, startStar, endStar);
        if(ans==-1) System.out.println("Impossible");
        else System.out.println(ans);

        sc.close();
    }

    static void dfs(int idx, Segment[] segs, boolean[] visited, Star s){
        if(visited[idx]) return;
        visited[idx]=true;
        s.addSegment(segs[idx]);
        for(int i=0;i<segs.length;i++){
            if(!visited[i]){
                Segment a = segs[idx], b = segs[i];
                if(pointOnSegment(a,b.x1,b.y1) || pointOnSegment(a,b.x2,b.y2) ||
                   pointOnSegment(b,a.x1,a.y1) || pointOnSegment(b,a.x2,a.y2)){
                    dfs(i,segs,visited,s);
                }
            }
        }
    }

    static boolean pointOnSegment(Segment s, int x, int y){
        return x>=Math.min(s.x1,s.x2) && x<=Math.max(s.x1,s.x2) &&
               y>=Math.min(s.y1,s.y2) && y<=Math.max(s.y1,s.y2) &&
               (slope(s.x1,s.y1,s.x2,s.y2)==slope(s.x1,s.y1,x,y));
    }

    static double slope(int x1,int y1,int x2,int y2){
        if(x1==x2) return Double.POSITIVE_INFINITY;
        return (double)(y2-y1)/(x2-x1);
    }
}
