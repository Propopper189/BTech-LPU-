// Abstract Class
abstract class a
{
    abstract void show();
}
class b extends a
{
    public void show()
    {
        System.out.println("Showing");
    }
}
public class practice17 {
    public static void main(String args[])
    {
        b obj1 = new b();
        obj1.show();
        a obj2 = new a()
        {
            public void show()
            {
                System.out.println("Anonymous class");
            }
        };
        obj2.show();
    }
}
