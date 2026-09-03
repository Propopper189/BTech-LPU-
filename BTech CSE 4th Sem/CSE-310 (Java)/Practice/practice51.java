import java.util.*;

class Student
{
    String name;
    int roll;
    Student(String name, int roll)
    {
        this.name = name;
        this.roll = roll;
    }
    public String toString()
    {
        return "Name: " + name + ", Roll: " + roll;
    }
}

class Sort implements Comparator<Student>
{
    public int compare(Student s1, Student s2)
    {
        return s1.name.compareTo(s2.name);
    }
}
public class practice51 {
    public static void main(String args[])
    {
        ArrayList<Student> st1 = new ArrayList<>();
        st1.add(new Student("Alice", 10));
        st1.add(new Student("Bob", 5)); 
        st1.add(new Student("Aquib", 15));

        Collections.sort(st1, new Sort());
        for(Student s : st1)
        {
            System.out.println(s);
        }
    }
}
