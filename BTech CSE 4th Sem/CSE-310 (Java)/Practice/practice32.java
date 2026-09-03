import java.util.Arrays;
import java.util.InputMismatchException;

class practice32
{
    public static void main(String args[])
    {
        try
        {
            int x = 10;
            int y = 20;
            System.out.println(x / y);
            int arr[] = new int[10];
            for(int i = 0; i < 10; i++)
            {
                arr[i] = i + 1;
                System.out.print(arr[i] + " ");
            }
            System.out.println();
            System.out.println(Arrays.toString(arr));
        }
        catch(ArrayIndexOutOfBoundsException e)
        {
            System.out.println(e.getMessage());
        }
        catch(ArithmeticException e)
        {
            System.out.println(e.getMessage());
        }
        catch(InputMismatchException e)
        {
            System.out.println(e.getMessage());
        }
        finally
        {
            System.out.println("Program Executed Successfully");
        }
    }
}