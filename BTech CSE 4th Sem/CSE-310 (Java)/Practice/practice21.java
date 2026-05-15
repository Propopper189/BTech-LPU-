class Outer
{
    class Inner
    {
        void show()
        {
            System.out.println("Inner");
        }
    }
}

class practice21
{
    public static void main(String args[])
    {
        Outer obj1 = new Outer();
        Outer.Inner obj2 = obj1.new Inner();
        obj2.show();
    }
}