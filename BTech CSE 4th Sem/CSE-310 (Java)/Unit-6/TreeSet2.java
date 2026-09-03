import java.util.*;

class Student {
    int roll;
    String name;

    Student(int roll, String name) {
        this.roll = roll;
        this.name = name;
    }
}

class SortName implements Comparator<Student> {
    public int compare(Student a, Student b) {
        return a.name.compareTo(b.name);
    }
}

public class TreeSet2 {
    public static void main(String args[]) {
        TreeSet<Student> st1 = new TreeSet<>(new SortName());

        st1.add(new Student(90, "B"));
        st1.add(new Student(80, "C"));
        st1.add(new Student(70, "A"));

        for (Student val : st1) {
            System.out.println(val.name + " " + val.roll);
        }
    }
}