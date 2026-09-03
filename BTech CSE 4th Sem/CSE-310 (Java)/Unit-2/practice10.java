// Write a program to accept a string and replace a particular substring with another substring
class practice10
{
    public static void main(String[] args)
    {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        String s = sc.nextLine();
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();
        s = s.replace(s1, s2);
        System.out.println(s);
    }
}