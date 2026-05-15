import java.io.*;
public class practice38 {
    public static void main(String args[])
    {
        try(FileWriter f1 = new FileWriter("practice38.txt", false))
        {
            f1.write("This is a sample text written to the file using try-with-resources.");
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
        finally
        {
            System.out.println("File writing operation completed.");
        }
        try(FileReader f2 = new FileReader("practice38.txt"))
        {
            int ch;
            while((ch = f2.read()) != -1)
            {
                System.out.print((char) ch);
            }
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
        finally
        {
            System.out.println("\nFile Reading Completed.");
        }
    }
}
