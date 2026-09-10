import java.util.*;

public class MirrorMath{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        String number = sc.nextLine().trim();
        String mirror = sc.nextLine().trim();

        List<Character> validDigits = new ArrayList<>();

        Map<Character, Character> sideMirror = new HashMap<>();
        sideMirror.put('0','0');
        sideMirror.put('1','1');
        sideMirror.put('4','4');
        sideMirror.put('8','8');

        Map<Character, Character> upDownMirror = new HashMap<>();
        upDownMirror.put('0', '0');
        upDownMirror.put('1', '1');
        upDownMirror.put('5', '5');
        upDownMirror.put('6', '5');
        upDownMirror.put('8', '8');
        upDownMirror.put('9', '8');

        for (int i = 0; i < number.length(); i++)
        {
            char d = number.charAt(i);
            char m = mirror.charAt(i);
            Character result = null;

            switch (m)
            {
                case 'L':
                case 'R':
                    result = sideMirror.get(d);
                    break;
                case 'U':
                case 'D':
                    result = upDownMirror.get(d);
                    break;
                case 'S':
                    result = d;
                    break;
            }

            if (result != null)
            {
                validDigits.add(result);
            }
        }

        if (validDigits.isEmpty())
        {
            System.out.print(0);
            return;
        }

        Collections.sort(validDigits);
        StringBuilder sb = new StringBuilder();
        boolean nonZeroStarted = false;
        for (char c : validDigits)
        {
            if (c != '0') nonZeroStarted = true;
            if (nonZeroStarted) sb.append(c);
        }
        if (sb.length() == 0) sb.append('0');
        System.out.print(sb.toString());

        sc.close();
    }
}
