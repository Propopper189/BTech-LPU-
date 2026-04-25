class practice8
{
    public static void main(String args[])
    {
        // Write a program to accept a string and replace every words 1st char with upper case
        java.util.Scanner sc = new java.util.Scanner(System.in);
        String s = sc.nextLine();
        String words [] = s.split(" ");
        for(int i = 0; i < words.length; i++)
        {
            words[i] = words[i].replace(words[i].charAt(0), (words[i].toUpperCase()).charAt(0));
        }
        for(String word : words)
        {
            System.out.print(word + " ");
        }
    }
}