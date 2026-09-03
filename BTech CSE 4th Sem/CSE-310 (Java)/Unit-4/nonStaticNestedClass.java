// 2. Non static nested class (inner class)

class outer
{
    class inner
    {
        void lpu()
        {
            System.out.println("I am from LPU");
        }
    }
}
class nonStaticNestedClass
{
    public static void main(String args[])
    {
        outer obj1 = new outer();
        outer.inner obj2 = obj1.new inner();
        obj2.lpu();
    }
}