// Static Inner Class
class Outer
{
    static class Inner
    {
        void show()
        {
            System.out.println("Inner");
        }
    }
}
class practice20
{
    public static void main(String args[])
    {
        Outer.Inner obj1 = new Outer.Inner();
        obj1.show();
    }
}