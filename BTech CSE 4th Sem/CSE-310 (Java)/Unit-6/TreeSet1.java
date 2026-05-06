import java.util.*;

public class TreeSet1 implements Comparable<TreeSet1>
{
    int roll;
    String name;
    TreeSet1(int roll, String name)
    {
        this.roll = roll;
        this.name = name;
    }
    @Override
    public int compareTo(TreeSet1 s)
    {
        // Roll Wise Sort
        // return this.roll - s.roll; // descending

        // Name Wise Sort
        return this.name.compareTo(s.name);
    }
    public static void main(String[] args) 
    {
        TreeSet<TreeSet1> st1 = new TreeSet<>();
        
        st1.add(new TreeSet1(90, "B"));
        st1.add(new TreeSet1(80, "C"));
        st1.add(new TreeSet1(70, "A"));
    
        for(TreeSet1 val : st1)
        {
            System.out.println(val.name + " " + val.roll);
        }
    }
}
