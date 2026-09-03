import java.util.*;
class practice31
{
    public static void main(String args[])
    {
        try
        {
            Scanner sc = new Scanner(System.in);
            int x = sc.nextInt();
            int y = sc.nextInt();
            System.out.println(x/y);
        }
        catch(InputMismatchException e)
        {
            System.out.println("Enter Intgers Only");
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
            System.out.println("Division By Zero Is Not Possible");
        }
        finally
        {
            System.out.println("Program Executed Successfully");
        }
    }
}