// Write a program to accept 2 strings and check they are anagram or not
class practice2
{
    public static void main(String args[])
    {
        // occurence of first string and occurence of second string should be same
        java.util.Scanner sc = new java.util.Scanner(System.in);
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();
        int hash[] = new int[256];
        for(int i = 0; i < s1.length(); i++)
        {
            hash[s1.charAt(i)]++;
        }
        for(int i = 0; i < s2.length(); i++)
        {
            hash[s2.charAt(i)]--;
        }
        for(int i = 0; i < hash.length; i++)
        {
            if(hash[i] != 0)
            {
                System.out.println("Not Anagram");
                System.exit(0); // program terminates from this line
            }
        }
        System.out.println("Anagram");
    }
}