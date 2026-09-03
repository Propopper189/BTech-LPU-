final class a 
{
    final int x = 10;
    a()
    {
        // x++; -> final variables can not be changed
        System.out.println("Value of x is : " + x);
    }
}   

// Final class cannot have a child
// class b extends a
// {
//     b()
//     {
//         System.out.println("Value of x : " + x);
//     }
// }

public class practice15 
{
    public static void main(String args[])
    {
        a obj = new a();
    }
}
