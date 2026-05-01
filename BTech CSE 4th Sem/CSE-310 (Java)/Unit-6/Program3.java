/*
    Write a program to join 2 lists
*/
import java.util.*;
public class Program3 {
    public static void main(String args[])
    {
        Integer arr1 [] = {1, 2, 3, 4, 5};
        Integer arr2 [] = {6, 7, 8, 9, 10};

        ArrayList<Integer> li1 = new ArrayList<>(Arrays.asList(arr1));
        ArrayList<Integer> li2 = new ArrayList<>(Arrays.asList(arr2));
        ArrayList<Integer> li3 = new ArrayList<>(Arrays.asList(1, 3, 4, 7)); // another method to create arraylist.

        // for(int j : li2)
        // {
        //     li1.add(j);
        // }

        li1.addAll(li2);
        System.out.println(li1);
    }
}
