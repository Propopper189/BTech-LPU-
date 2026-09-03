class practice3 {
    public static void main(String args[])
    {
        java.util.Scanner sc = new java.util.Scanner(System.in);

        int n = sc.nextInt();
        char arr[] = new char[n];

        for(int i = 0; i < n; i++)
        {
            arr[i] = sc.next().charAt(0);
        }

        int hash[] = new int[26];

        // Count frequency
        for(int i = 0; i < n; i++)
        {
            hash[arr[i] - 'a']++;
        }

        // Print result
        for(int i = 0; i < 26; i++)
        {
            if(hash[i] != 0)
            {
                char ch = (char)(i + 'a');
                System.out.println(ch + " present " + hash[i] + " times");
            }
        }
    }
}
