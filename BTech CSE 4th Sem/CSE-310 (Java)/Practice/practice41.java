import java.io.*;
public class practice41 {
    public static void main(String args[])
    {
        try
        {
            // FileOutputStream
            FileOutputStream f1 = new FileOutputStream("practice41.txt");
            String s = "Hello World";
            byte b[] = s.getBytes();
            f1.write(b);
            f1.close();

            // FileInputStream
            FileInputStream f2 = new FileInputStream("practice41.txt");
            int ch;
            while((ch = f2.read()) != -1)
            {
                System.out.print((char)ch);
            }
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
        finally
        {
            System.out.println("\nFile operations completed.");
        }
    }
}
