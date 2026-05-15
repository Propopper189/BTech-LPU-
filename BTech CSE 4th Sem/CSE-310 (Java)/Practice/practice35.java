public class practice35 {
    static void checkAge(int age) throws Exception
    {
        if(age < 18)
        {
            throw new Exception("Age is under 18");
        }
        System.out.println("Age >= 18");
    }
    public static void main(String args[])
    {
        try
        {
            checkAge(2);
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}