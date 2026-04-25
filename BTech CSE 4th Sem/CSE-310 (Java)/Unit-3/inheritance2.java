class A
{   
    int x = 5;
}
class inheritance2 extends A
{
    int y = 6;
    void dis()
    {
        System.out.println(x);
        System.out.println(y);
    }
    public static void main(String args[])
    {
        inheritance2 objB = new inheritance2();
        objB.dis();
        System.out.println(objB.x * objB.y);
    }
}
