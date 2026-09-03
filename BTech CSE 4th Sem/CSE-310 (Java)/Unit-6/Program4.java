import java.util.*;

public class Program4 {
    /*
        Write a program to merge two lists
    */
   public static void main(String args[])
   {
        Integer arr1 [] = {1, 2, 3, 4, 5};
        Integer arr2 [] = {6, 8, 7, 10, 9};

        ArrayList<Integer> li1 = new ArrayList<>(Arrays.asList(arr1));
        ArrayList<Integer> li2 = new ArrayList<>(Arrays.asList(arr2));
        
        li1.addAll(li2);
        Collections.sort(li1);
        System.out.println(li1);
   }
}
