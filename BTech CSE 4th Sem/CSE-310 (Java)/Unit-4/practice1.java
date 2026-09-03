/*
Write a program to accept a number from the user and add all the odd digits.
*/
class practice1
{
    public static void main(String args[])
    {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0;
        while(n != 0)
        {
            int odd = n % 10;
            if(odd % 2 != 0)
            {
                sum = sum + odd;
            }
            n = n/10;
        }
        System.out.println(sum);
    }
}