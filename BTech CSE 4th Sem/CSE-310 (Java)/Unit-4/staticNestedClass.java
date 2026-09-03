/*
Nested Class : 
    A class within another class is called as nested class.

    2 Types of Nested Class : 
        a. static nested class
        b. inner class (non static nested class)
*/
class outer
{
    static class inner // static nested class.
    {
        void lpu()
        {
            System.out.print("I am from LPU");
        }
    }
}
class staticNestedClass
{
    public static void main(String args[])
    {
        outer.inner obj = new outer.inner();
        obj.lpu();
    }
}