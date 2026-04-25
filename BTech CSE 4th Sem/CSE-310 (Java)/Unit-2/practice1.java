// Write a program to remove the duplicate elements from an array
import java.util.*;
class practice1
{
    public static void main(String args[])
    {
        int arr[] = {3, 1, 3, 2, 1, 3, 4, 2, 1};
        // Set<Integer> st = new HashSet<>(); -> it will sort.
        Set<Integer> st = new LinkedHashSet<>();
        // To maintain the original order.
        for(int i = 0; i < arr.length; i++)
        {
            st.add(arr[i]);
        }
        System.out.println(st);
    }
}