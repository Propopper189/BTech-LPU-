import java.util.*;

public class practice49 {
    public static void main(String args[])
    {
        TreeSet<Integer> set = new TreeSet<>();
        // add
        set.add(20);
        set.add(10);
        set.add(30);
        set.add(10); // duplicate ignored
        System.out.println("TreeSet: " + set);
        // contains
        System.out.println("Tree Contains 20 ? : " + set.contains(20));
        // remove
        set.remove(30); 
        System.out.println("TreeSet after removal: " + set);
        // size 
        System.out.println("Size: " + set.size());
        // iterate
        for(int i = 0; i < set.size(); i++)
        {
            // System.out.println(set.get(i)); // TreeSet does not support get() method
            System.out.println("Element at index " + i + ": " + set.toArray()[i]); // Convert to array for indexed access
        }
        System.out.println("Iterating another time :");
        for(int i = 0; i < set.size(); i++)
        {
            System.out.println("Element at index " + i + ": " + set.toArray()[i]); // Convert to array for indexed access
        }
    }    
}
