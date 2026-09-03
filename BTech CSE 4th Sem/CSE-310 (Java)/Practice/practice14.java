// Method Overriding
class a
{
    int x = 10;
    void show()
    {
        System.out.println("Showing");
    }
}
class b extends a
{
    int x = 20;
    @Override
    public void show()
    {
        System.out.println("Overriding");
        System.out.println("Value of x in " + getClass() + " is : " + x);
        System.out.println("Value of x in parent class a" + " is : " + super.x);
    }
}
public class practice14 {
    public static void main(String args[])
    {
        a obj = new b();
        obj.show();
    }
}
