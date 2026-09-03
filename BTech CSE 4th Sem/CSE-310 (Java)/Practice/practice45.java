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
    public String toString()
    {
        return roll + " " + name;
    }
}
class practice45
{
    public static void main(String args[])
    {
        Student s1 = new Student(10, "Aquib");
        try
        {
            ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("practice45.txt"));
            oos.writeObject(s1);
            oos.close();

            ObjectInputStream ois = new ObjectInputStream(new FileInputStream("practice45.txt"));
            Student s2;
            while((s2 = (Student) ois.readObject()) != null)
            {
                System.out.println(s2);
            }
            ois.close();    
        }
        catch(Exception e)
        {
            // System.out.println(e.getMessage());
        }
    }
}