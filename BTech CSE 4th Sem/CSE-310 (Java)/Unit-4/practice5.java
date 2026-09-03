
abstract class a
{
    abstract void add(int a, int b);
}
class practice5
{
    public static void main(String args[])
    {
        a obj = new a()
        {
            void add(int a, int b)
            {
                System.out.println("The sum of the two numbers is : " + (a + b));
            }
        };
        obj.add(1, 3);
    }
}