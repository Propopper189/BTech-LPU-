interface a
{
    void show();
}
class b implements a
{
    public void show()
    {
        System.out.println("Overriding Show Method Of Inteface a");
    }
}

class practice18
{
    public static void main(String args[])
    {
        b obj1 = new b();
        obj1.show();

        a obj2 = new a()
        {
            public void show()
            {
                System.out.println("Anonymous Class");
            }
        };
        obj2.show();

        a obj3 = () ->
        {
            System.out.println("Lambda Function");
        };
        obj3.show();
    }
}
