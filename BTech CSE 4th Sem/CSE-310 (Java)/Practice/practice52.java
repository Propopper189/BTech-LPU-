import java.util.*;

public class practice52 {
    public static void main(String args[])
    {
        String s = "abcaabbcccdd";
        HashMap<Character, Integer> mp = new HashMap<>();
        // Count The Frequency Of Each Character
        for(int i = 0; i < s.length(); i++)
        {
            if(!mp.containsKey(s.charAt(i)))
            {
                mp.put(s.charAt(i), 1);
            }
            else
            {
                mp.put(s.charAt(i), mp.get(s.charAt(i)) + 1);
            }
        }
        // Print The Frequency Of Each Character
        for(Map.Entry<Character, Integer> entry : mp.entrySet())
        {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }
        System.out.println("The Frequency Of Character 'a' : " + mp.get('a'));
        System.out.println("Removing The Character 'a' From The HashMap");
        mp.remove('a');
        System.out.println("The Frequency Of Character 'a' : " + mp.get('a'));
        System.out.println("Contains Value 2 ? : " + mp.containsValue(2));
        for(Map.Entry<Character, Integer> entry : mp.entrySet())
        {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }    
}
