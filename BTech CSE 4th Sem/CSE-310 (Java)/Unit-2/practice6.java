// write a program to convert every 
// words 1st character to UpperCase
class practice6
{
    public static void main(String args[])
    {
        String s1 = "i am from lpu";
        String words [] = s1.split(" ");
        // String temp;
        for(int i = 0; i < words.length; i++)
        {
            words[i] = words[i].concat("");
            // temp = words[i].toUpperCase();
            words[i] = words[i].replace(words[i].charAt(0), (words[i].toUpperCase()).charAt(0));
        }
        for(String word : words)
        {
            s1 = s1.concat(word + " ");
        }
        System.out.println(java.util.Arrays.toString(words));
    }
}