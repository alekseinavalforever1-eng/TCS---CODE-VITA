// Question - StringQuest
// Raju and Rani like playing with strings, exploring the interesting patterns of smaller parts within them,
// called substrings.
// Presently, they are engrossed in a string-centric game and it is Raju's turn. His task involves two strings
// provided by Rani, namely S1 and S2. Raju is tasked with dividing the first string S1 into the fewest possible
// substrings, ensuring that all resulting substrings, whether in their original or reversed order, are present in
// S2 while also aiming for maximizing the length of current substring.
// For example, if S1 = "vanaja" and S2 = "rvanpnaja", then the output will be van|aja rather than va|naja.
// Note : The letter in the i
// th position in S1 can be used in exactly one substring of S1. The letters from S2 can
// be reused any number of times but the letters from S1 can be used only once. The letters are case sensitive
// in both the strings.
// Constraints
// 1 <= S1, S2 <= 10000
// The two strings S1, S2 consist of lower and upper case characters only.
// Input
// First line consists of a string S1.
// Second line consists of string S2.
// Output
// Print the string S1 as a concatenation of sub strings separated by '|'.
// Time Limit (secs)
// 1
// Examples
// Example 1
// Input
// VaisHnavI
// VIvekanandaJasHnavi
// Output
// V|a|i|sHnav|I
// Explanation
// Every sub string that is present in V|a|i|sHnav|I is also present in S2 in original or reversed order. No other
// way of doing sub strings on S1 will give less number of sub strings than this. Hence, we print V|a|i|sHnav|I.
// Example 2
// Input
// sudHanShu
// qniwprvAvnaHSsH
// Output
// Impossible
// Explanation
// As we can see, its impossible to sub string the string S1 based given conditions, thus we print "Impossible".

import java.util.*;

public class SubStringQuest {

    public static void main(String[] args) {
        Scanner x = new Scanner(System.in);
        String a = x.nextLine();
        String b = x.nextLine();
        System.out.print(stringQuest(a, b));
        x.close();
    }
    private static String reverse(String r) {
        String s = "";
        for (int i = r.length() - 1; i >= 0; i--)
            s += r.charAt(i);
        return s;
    }

    private static String stringQuest(String a, String b) {
        int i = 0;
        String res = "";
        while (i < a.length()) {
            boolean flag = false;
            for (int j = a.length(); j >= i + 1; j--) {
                String s = a.substring(i, j);
                if (b.contains(s) || b.contains(reverse(s))) {
                    if (!res.equals(""))
                        res += "|" + s;
                    else
                        res += s;
                    i = j;
                    flag = true;
                    break;
                }
            }
            if (!flag)
                return "Impossible";
        }
        return res;
    }
}