/*
    Write a program to delete all even numbers from the array
*/
import java.util.*;
public class Program2 {
    public static void main(String args[])
    {
        int arr[] = {5, 12, 7, 4, 6, 8, 13};
        ArrayList<Integer> li = new ArrayList<>();
        for(int j : arr)
        {
            li.add(j);
        }
        li.removeIf(x->x%2 == 0); // check if x even, and if yes, delete it.
        System.out.println(li);
    }
}
