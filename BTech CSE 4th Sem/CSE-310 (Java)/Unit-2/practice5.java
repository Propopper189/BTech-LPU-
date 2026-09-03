// Write a program to find the length of last word from a string
class practice5
{
    public static void main(String args[])
    {
        String a = "i dont want to study";
        String words[] = a.split(" ");
        System.out.println((words[words.length - 1]).length());
    }
}