public class practice33 {
    public static void main(String args[])
    {
        // Nested Try-Catch
        try
        {
            try
            {
                int x = 10;
                int y = 5;
                System.out.println(x / y);
            }
            catch(ArithmeticException e)
            {
                System.out.println(e.getMessage());
                throw new Exception("Catch It");
            }
        }
        catch(Exception e)
        {
            System.out.println("Outer Catch");
        }
        finally
        {
            // This block will execute even if Exception is caught
            System.out.println("Program Executed Successfully");
        }
    }
}
