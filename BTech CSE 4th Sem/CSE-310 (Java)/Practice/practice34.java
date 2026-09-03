public class practice34 {
    public static void main(String args[])
    {
        try
        {
            int age = 17;
            if(age < 18)
            {
                throw new Exception("Age is under 18");
            }
            System.out.println("Age >= 18");
        }        
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}
