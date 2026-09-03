// write a program to accept 2 strings and check if its anagram
class practice3
{
    public static void main(String args[])
    {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();
        char sa1[] = s2.toCharArray();
        char sa2[] = s1.toCharArray();
        java.util.Arrays.sort(sa1);
        java.util.Arrays.sort(sa2);
        if(java.util.Arrays.equals(sa1, sa2))
        {
            System.out.println("Anagram");
        }
        else
        {
            System.out.println("not anagram");
        }
    }
}