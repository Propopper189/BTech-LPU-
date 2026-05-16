import java.util.*;

class practice48
{
    public static void main(String args[])
    {
        HashSet<Integer> set = new HashSet<>();

        // add
        set.add(10);
        set.add(20);
        set.add(30);
        set.add(10); // duplicate ignored

        System.out.println("HashSet: " + set);

        // contains
        System.out.println(set.contains(20));

        // remove
        set.remove(30);

        // size
        System.out.println("Size: " + set.size());

        // iterate
        for(int x : set)
        {
            System.out.println(x);
        }

        // clear
        set.clear();

        System.out.println("Empty? " + set.isEmpty());
    }
}