import java.util.*;
public class Main{
    static double e=1e-9;
    static double ax,ay,bx,by;
    static double[] L;
    static int k,n;
    static double sx,sy;
    static double[] sim(){
        double x=sx,y=sy,vx=-1,vy=1;
        int c=0;
        ArrayList<Double> z=new ArrayList<>();
        for(int t=0;t<2000;t++){
            double tx=vx>0?bx-x:(vx<0?x-ax:1e18);
            double ty=vy>0?by-y:(vy<0?y-ay:1e18);
            double tp=vy<0? (y-sy>0?y-sy:1e18):1e18;
            double dt=Math.min(tx,Math.min(ty,tp));
            if(dt>1e17)break;
            x+=vx*dt;y+=vy*dt;
            boolean hv=Math.abs(dt-tx)<e&&vx!=0;
            boolean hh=Math.abs(dt-ty)<e&&vy!=0;
            boolean hp=Math.abs(dt-tp)<e&&vy<0;
            if(hp){
                z.add(x);
                double le=sx-n/2.0,ri=sx+n/2.0;
                if(Math.abs(x-le)<e){vx=-1;vy=1;}
                else if(Math.abs(x-ri)<e){vx=1;vy=1;}
                else vy=1;
                continue;
            }
            if(hv){vx=-vx;c++;}
            if(hh){vy=-vy;c++;}
            if(c>=k)break;
        }
        double[] r=new double[z.size()+1];
        for(int i=0;i<z.size();i++)r[i]=z.get(i);
        r[z.size()]=Math.min(L[1],c);
        return r;
    }
    static boolean ok(int d,double[] a){
        if(a.length==1)return true;
        double h=n/2.0;
        double lo=a[0]-h,hi=a[0]+h;
        lo=Math.max(lo,sx-d);
        hi=Math.min(hi,sx+d);
        if(lo>hi+e)return false;
        for(int i=1;i<a.length-1;i++){
            double t=a[i];
            double lo2=t-h,hi2=t+h;
            lo=lo-d;hi=hi+d;
            lo=Math.max(lo,lo2);
            hi=Math.min(hi,hi2);
            if(lo>hi+e)return false;
        }
        return true;
    }
    static int bs(double[] a){
        int l=0,r=(int)(bx-ax)+5,ans=r;
        while(l<=r){
            int m=(l+r)/2;
            if(ok(m,a)){ans=m;r=m-1;}
            else l=m+1;
        }
        return ans;
    }
    public static void main(String[] args){
        Scanner s=new Scanner(System.in);
        k=s.nextInt();
        sx=s.nextDouble(); sy=s.nextDouble();
        n=s.nextInt();
        ax=s.nextDouble(); ay=s.nextDouble(); bx=s.nextDouble(); by=s.nextDouble();
        L=new double[2];
        double[] a=sim();
        int d=bs(a);
        System.out.println(d);
    }
}
