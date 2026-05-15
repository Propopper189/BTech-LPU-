@FunctionalInterface
interface a
{
    void show();
}
interface c
{
    void display(int a, int b);
}
class b implements a, c
{
    public void show()
    {
        System.out.println("Overriding Interface A Method");
    }
    public void display(int a, int b)
    {
        System.out.println("Overriding Interface C Method");
        System.out.println(a + b);
    }
}
public class practice22 
{
    public static void main(String args[])
    {
        b obj1 = new b();
        obj1.show();
        obj1.display(10, 20);

        a obj2 = new a()
        {
            public void show()
            {
                System.out.println("Anonymous Class");
            }
        };
        obj2.show();
        c obj3 = (a, b) ->
        {
            System.out.println("Lambda Function");
            System.out.println(a + b);
        };
        obj3.display(10, 20);
    }
}
