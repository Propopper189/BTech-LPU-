import java.io.*;

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
public class practice43 {
    public static void main(String args[])
    {
        try
        {
            FileOutputStream fos = new FileOutputStream("practice43.txt");
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            Student s1 = new Student(1, "John");
            oos.writeObject(s1);
            oos.close();

            try
            {
                FileInputStream fis = new FileInputStream("practice43.txt");
                ObjectInputStream ois = new ObjectInputStream(fis);
                Student s2 = (Student) ois.readObject();
                ois.close();
                System.out.println("Roll : " + s2.roll);
                System.out.println("Name : " + s2.name);
            }
            catch(Exception e)
            {
                System.out.println("Error : " + e.getMessage());
            }
        }
        catch(IOException e)
        {
            System.out.println("Error : " + e.getMessage());
        }
    }
}
