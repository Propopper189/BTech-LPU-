// Write a program to accept 2 numbers from the user and find the greatest number using Lambda Expression
interface a
{
    void greater(int a, int b);
}
class practice3
{
    public static void main(String args[])
    {
        a obj = (a, b)->
        {
            int c = Math.max(a, b);
            System.out.println("Greater Number : " + c);
        };
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        obj.greater(a, b);
    }
}