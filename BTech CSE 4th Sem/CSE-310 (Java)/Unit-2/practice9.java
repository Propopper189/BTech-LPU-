// Write a program to accept a string and if the string contains one word reverse it
// if the string contains 2 words, join it, if the string contains more than 2 word
// print invalid input

class practice9
{
    public static void main(String args[])
    {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        String s = sc.nextLine();
        String words[] = s.split(" ");
        if(words.length == 1)
        {
            StringBuilder sb = new StringBuilder(s);
            sb.reverse();
            s = sb.toString();
        }
        else if(words.length == 2)
        {
            s = "";
            for(String word : words)
            {
                s = s.concat(word);
            }
        }
        else
        {
            System.out.println("Invalid Input");
            return;
        }
        System.out.print(s);
    }
}