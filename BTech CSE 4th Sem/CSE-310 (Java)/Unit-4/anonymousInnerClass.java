/*
Anonymous Inner Class : 
    A class without name
    It is required when immediately we want to override an abstract method without being a child.
*/
abstract class a
{
    abstract void abc();
}
class anonymousInnerClass
{
    public static void main(String args[])
    {
        // Anonymous Class
        a obj = new a()
        {
            void abc()
            {
                System.out.println("Overriden Method");
            }
        };
        obj.abc();
    }
}