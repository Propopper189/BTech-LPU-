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
    }
}
