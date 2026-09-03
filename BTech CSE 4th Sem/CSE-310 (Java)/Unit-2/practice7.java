class practice7
{
    // Write a program to accept a string and coutn the occurence of every character
    public static void main(String args[])
    {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        String s = sc.nextLine();
        int hash[] = new int[123];
        for(int i = 0; i < s.length(); i++)
        {
            char ch = s.charAt(i);
            hash[ch]++;
        }
        for(int i = 0; i < s.length(); i++)
        {
            if(hash[s.charAt(i)] != 0)
            {
                if(s.charAt(i) == ' ')
                {
                    System.out.print("Space : ");
                    System.out.println( hash[s.charAt(i)]);
                    hash[s.charAt(i)] = 0;
                    continue;
                }
                System.out.println(s.charAt(i) + " " + hash[s.charAt(i)]);
                hash[s.charAt(i)] = 0;
            }
        }
    }
}