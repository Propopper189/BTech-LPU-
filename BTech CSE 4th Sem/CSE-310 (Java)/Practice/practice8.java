// class and object
class Student
{
    int id;
    String name;

    Student(int id, String name)
    {
        this.id = id;
        this.name = name;
    }

    String display()
    {
        return ("ID : " + this.id + " | Name : " + this.name); 
    }
    public String toString()
    {
        return display();
    }
}
public class practice8 {
    public static void main(String args[])
    {
        Student std = new Student(10, "Aquib");
        System.out.println(std);
        Student std1 = new Student(11, "Jawaid");
        System.out.println(std1);
    }
}
