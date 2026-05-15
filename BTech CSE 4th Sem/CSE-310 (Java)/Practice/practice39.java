import java.util.*;
public class practice39 {
    public static void main(String args[])
    {
        /*
        📌 FINAL EXAM LINE
        👉 Buffer clearing is required because:
        Scanner methods like nextInt(), nextDouble(), 
        next() do not consume newline character, which 
        interferes with nextLine() input.
        */
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        String s = sc.next();
        sc.nextLine(); // Clear the buffer
        String line = sc.nextLine();
        System.out.println("Integer: " + a);
        System.out.println("String: " + s);
        System.out.println("Line: " + line);    
    }
}
