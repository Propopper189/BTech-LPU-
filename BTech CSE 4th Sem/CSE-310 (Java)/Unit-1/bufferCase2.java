// Write a program to accept a word and then string(Line) and display
import java.util.*;

class bufferCase2
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        sc.nextLine(); // Adding a buffer (word then string) mandatory
        String name = sc.nextLine();
        System.out.printf("Word : %s | String : %s", word, name);
    }
}