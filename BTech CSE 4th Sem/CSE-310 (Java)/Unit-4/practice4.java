// Write a program to find factorial of a number using lambda expression;
interface a
{
    void factorial(int n);
}
class practice4
{
    public static void main(String args[])
    {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        a obj = (m)->
        {
            int a = 1;
            for(int i = 2; i <= m; i++)
            {
                a *= i;
            }
            System.out.println("Factorial of " + n + " is : " + a);
        };
        obj.factorial(n);
    }
}