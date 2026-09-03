// Write a program to reverse a String using anonymous inner class
abstract class a
{
    abstract void rev(String a);
}
class practice6
{
    public static void main(String args[])
    {
        a obj = new a()
        {
            void rev(String a)
            {
                StringBuilder sb = new StringBuilder(a);
                sb.reverse();
                a = sb.toString();
                System.out.println("The reversed String is : " + a);
            }
        };
        java.util.Scanner sc = new java.util.Scanner(System.in);
        String st = sc.nextLine();
        obj.rev(st);
    }
}