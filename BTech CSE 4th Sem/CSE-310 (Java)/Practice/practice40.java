import java.io.*;
public class practice40 {
    public static void main(String args[]) throws Exception
    {
        FileWriter fw = new FileWriter("practice40.txt");
        fw.write("Hello\nWorld");
        fw.close();
        FileReader fr = new FileReader("practice40.txt");
        int ch;
        while((ch = fr.read()) != -1)
        {
            System.out.print((char) ch);
        }
        fr.close();
    }
}
