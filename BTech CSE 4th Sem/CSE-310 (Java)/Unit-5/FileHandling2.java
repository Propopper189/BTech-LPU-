/*
Write a program to read and write using Byte Stream 
*/
import java.io.*;

class FileHandling2 {
    public static void main(String args[]) throws IOException
    {
        // Open the file in write mode 
        FileOutputStream f1 = new FileOutputStream("FileHandling2.txt");
        // f1.write("I am a student"); (We cannot write like this)
        
        // Create a string
        String s = "I am a student";

        // Convert the string to byte array
        byte a[] = s.getBytes();
        
        // Write the byte array
        f1.write(a);
        f1.close();

        // Read the file
        FileInputStream f2 = new FileInputStream("FileHandling2.txt");
        int ch;
        while((ch=f2.read()) != -1)
        {
            System.out.print((char)ch);
        }
    }
    
}
