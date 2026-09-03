import java.util.*;

class Student implements Comparable<Student>
{
    String name;
    int roll;
    Student(int roll, String name)
    {
        this.roll = roll;
        this.name = name; 
    }
    public int compareTo(Student s)
    {
        return this.name.compareTo(s.name);
    }
    public String toString()
    {
        return "Name : " + name + " Roll : "  + roll;
    }

}
public class practice50 {
    public static void main(String args[])
    {
        TreeSet<Student> ts = new TreeSet<>();
        ts.add(new Student(1, "Aquib"));
        ts.add(new Student(2, "Jawaid"));
        ts.add(new Student(0, "Ball"));
        for(int i = 0; i < ts.size(); i++)
        {
            System.out.println(ts.toArray()[i]);
        }
    }
}
