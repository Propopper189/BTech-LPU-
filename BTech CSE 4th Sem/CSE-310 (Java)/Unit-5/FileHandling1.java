/*
1) Char Stream
    - FileWriter (Open the file in write mode)
    - FileReader (Open the file in read mode)

2) Byte Stream
    - FileOutputStream 
    - FileInputStream 

Write a program to open a file in write mode, write some texts and read it character wise

*/

import java.io.*;
class FileHandling1
{
    public static void main(String args[]) throws IOException
    {
        // FileWriter f1 = new FileWriter("FileHandling1.txt"); (does not allow append)
        FileWriter f1 = new FileWriter("FileHandling1.txt"); 
        f1.write("Hello\n");
        f1.write("I am a student\n");
        f1.close();
        System.out.println("File Written Successfully!");

        FileWriter f3 = new FileWriter("FileHandling1.txt", true); // true -> Enable Append
        f3.write("I am from 324KP");
        f3.close();

        // Read A File
        FileReader f2 = new FileReader("FileHandling1.txt");
        int ch;
        while((ch=f2.read()) != -1)
        {
            System.out.print((char) ch);
        }
        f2.close();
    }
}