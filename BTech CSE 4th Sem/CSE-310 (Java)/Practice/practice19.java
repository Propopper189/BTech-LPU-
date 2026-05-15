interface a
{
    static void hi()
    {
        System.out.println("Hi");
    }
    default void show()
    {
        System.out.println("Showing Interface Method " + '"' + "show" + '"');
    }
}

class b implements a
{

}
public class practice19 {
    public static void main(String args[])
    {
        a.hi();
        b obj = new b();
        obj.show();
    }
}
