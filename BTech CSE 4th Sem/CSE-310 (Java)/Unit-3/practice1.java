// Write a program to accept a string and check whether its palindrome or not.
class practice1
{
    public static void main(String args[])
    {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        String s = sc.nextLine();
        StringBuilder sb = new StringBuilder(s);
        sb.reverse();
        String rs = sb.toString();
        if(s.equalsIgnoreCase(rs)) // Ignores the case (upper/lower) and compares the string
        {
            System.out.println("Palindrome");
        }
        else
        {
            System.out.println("Not Palindrome");
        }
    }
}