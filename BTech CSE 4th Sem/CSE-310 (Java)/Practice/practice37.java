public class practice37 
{
    public static void main(String args[])
    {
        try
        {
            int a = 10, b = 0;
            int c = a / b;
            int arr[] = new int[5];
            arr[10] = 50;
            System.out.print(c);
        }
        catch(ArithmeticException | ArrayIndexOutOfBoundsException e1)
        {
            System.out.println("An error occurred " + e1.getMessage());
        }
    }    
}
