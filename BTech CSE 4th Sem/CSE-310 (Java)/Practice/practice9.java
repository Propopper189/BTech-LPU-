// Constructor overloading
class A
{
    A()
    {
        // System.out.print(getClass());
        System.out.println("Created an object of " + getClass() + " without parameter");
    }
    A(int x)
    {
        System.out.println("Created object of " + getClass() + " with parameter : " + x);
    }
}
public class practice9 {
    public static void main(String args[])
    {
        A obj1 = new A();
        A obj2 = new A(2);
    }
}
