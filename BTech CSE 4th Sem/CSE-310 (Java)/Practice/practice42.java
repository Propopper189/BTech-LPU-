import java.io.*;
public class practice42 {
    public static void main(String args[]) throws IOException
    {
        BufferedWriter bw = new BufferedWriter(new FileWriter("practice42.txt"));
        String str = "Hi, This is practice42 content\nThis is the second line of the file.";
        bw.write(str);
        bw.close();

        BufferedReader br = new BufferedReader(new FileReader("practice42.txt"));
        String line;
        while((line = br.readLine()) != null)
        {
            System.out.println(line);
        }
        // br.readLine() will read the first line of the file and return it as a String. 
        // If there are multiple lines, you can call br.readLine() multiple times to read each line
        //  until it returns null (indicating the end of the file).  
        br.close();
    }
}
