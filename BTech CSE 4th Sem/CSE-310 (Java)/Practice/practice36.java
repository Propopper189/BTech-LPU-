class A extends Exception
{
    A(String s)
    {
        super(s);
    }
}
class b
{
    static void checkAge(int age) throws A
    {
        if(age < 18)
        {
            throw new A("Age is under 18");
        }
        System.out.println("Age >= 18");
    }   
}
class practice36
{
    public static void main(String args[])
    {
        try
        {
            b.checkAge(16);
            throw new A("This is a custom exception");
        }
        catch(A e)
        {
            System.out.println(e.getMessage());
        }
    }
}