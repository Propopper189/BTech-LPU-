class A
{
    int x = 5;
}

class B extends A
{
    int y = 6;
    void dis()
    {
        System.out.println("A : " + x);
        System.out.println("B : " + y);
        System.out.println("X + Y : " + (x + y));
    }
}
class inheritance1
{
    public static void main(String args[])
    {
        B objB = new B();
        objB.dis();
    }
}