import java.util.*;

public class BoxGame {
    static int N, K;
    static char[][][] cube = new char[6][][];
    static String[] instructions;
    static String[] faceNames = {"base","back","top","front","left","right"};
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        K = sc.nextInt();
        sc.nextLine();
        
        for(int f=0; f<6; f++){
            cube[f] = new char[N][N];
            for(int i=0;i<N;i++){
                String[] row = sc.nextLine().split(" ");
                for(int j=0;j<N;j++) cube[f][i][j] = row[j].charAt(0);
            }
        }
        
        instructions = new String[K];
        for(int i=0;i<K;i++) instructions[i] = sc.nextLine();
        
        String result = simulateCube();
        System.out.println(result);
        sc.close();
    }
    
    static String simulateCube(){
        char[][][] tempCube = copyCube(cube);
        
        for(int i=0;i<K;i++){
            boolean success = applyInstruction(tempCube, instructions[i]);
            if(!success){
                // Extra instruction
                if(isFaulty(tempCube)){
                    return "Faulty\n" + instructions[i];
                } else {
                    return instructions[i];
                }
            }
        }
        
        if(isAnySideSolved(tempCube)) return "Not Possible";
        return "Not Possible";
    }
    
    static boolean isFaulty(char[][][] c){
        // Check if any cube has different colors than original
        for(int f=0;f<6;f++)
            for(int i=0;i<N;i++)
                for(int j=0;j<N;j++)
                    if(c[f][i][j]!=cube[f][i][j])
                        return true;
        return false;
    }
    
    static boolean isAnySideSolved(char[][][] c){
        for(int f=0;f<6;f++){
            char first = c[f][0][0];
            boolean solved = true;
            for(int i=0;i<N;i++)
                for(int j=0;j<N;j++)
                    if(c[f][i][j]!=first) solved=false;
            if(solved) return true;
        }
        return false;
    }
    
    static boolean applyInstruction(char[][][] c, String inst){
        try{
            inst = inst.toLowerCase();
            if(inst.equals("turn left")) { turnLeft(c); return true; }
            else if(inst.equals("turn right")) { turnRight(c); return true; }
            else if(inst.equals("rotate front")) { rotateFront(c); return true; }
            else if(inst.equals("rotate back")) { rotateBack(c); return true; }
            else if(inst.equals("rotate left")) { rotateLeft(c); return true; }
            else if(inst.equals("rotate right")) { rotateRight(c); return true; }
            else {
                // side row/col rotation: e.g. "top 1 left" or "front 2 down"
                String[] parts = inst.split(" ");
                if(parts.length!=3) return false;
                String side = parts[0];
                int idx = Integer.parseInt(parts[1])-1;
                String dir = parts[2];
                return rotateRowCol(c, side, idx, dir);
            }
        } catch(Exception e){
            return false;
        }
    }
    
    static char[][][] copyCube(char[][][] c){
        char[][][] copy = new char[6][][];
        for(int f=0;f<6;f++){
            copy[f] = new char[N][N];
            for(int i=0;i<N;i++)
                System.arraycopy(c[f][i], 0, copy[f][i], 0, N);
        }
        return copy;
    }
    
    // Placeholder functions for rotations (detailed implementation required)
    static void turnLeft(char[][][] c){ /* Implement according to rules */ }
    static void turnRight(char[][][] c){ /* Implement according to rules */ }
    static void rotateFront(char[][][] c){ /* Implement according to rules */ }
    static void rotateBack(char[][][] c){ /* Implement according to rules */ }
    static void rotateLeft(char[][][] c){ /* Implement according to rules */ }
    static void rotateRight(char[][][] c){ /* Implement according to rules */ }
    
    static boolean rotateRowCol(char[][][] c, String side, int idx, String dir){
        // Implement row/col rotation rules
        // Return true if successful
        return true; // placeholder
    }
}
