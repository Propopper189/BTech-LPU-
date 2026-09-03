import java.io.*;
/*
    Serialization in file
        - Converting object to byte, and then store it in a file
        - Main purpose is to send it over the network.
    
    Deserialization in file
        - Converting bytes to object.
*/
class Student implements Serializable
{
    int roll;
    String name;
    Student(int roll, String name)
    {
        this.roll = roll;
        this.name = name;
    }
}
class FileHandling3
{
    public static void main(String args[]) throws IOException
   {
        // Serialization
        FileOutputStream f1 = new FileOutputStream("FileHandling3.txt");
        ObjectOutputStream out = new ObjectOutputStream(f1);
        Student s1 = new Student(10, "Aquib");
        out.writeObject(s1);
        System.out.println("Serialization Done");
        
        // De-Serialization
        try
        {
            FileInputStream f2 = new FileInputStream("FileHandling3.txt");
            ObjectInputStream in = new ObjectInputStream(f2);        
            Student s2 = (Student) in.readObject();
            System.out.println("Name : " + s2.name);
            System.out.println("Roll : " + s2.roll);
            System.out.println("De-Serialization Done");
        }
        catch(Exception e)
        {

        }
        



   }
}
