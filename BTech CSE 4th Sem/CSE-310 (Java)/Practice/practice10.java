// Method Overloading
class A
{
    static void intAdd(int a, int b)
    {
        System.out.println(a + b);
    }
    static void doubleAdd(double a, double b)
    {
        System.out.println(a + b);
    }
}
public class practice10 {
    public static void main(String args[])
    {
        A.intAdd(10, 20);
        A.doubleAdd(10.1, 20.3);
    }
}
