import java.util.*;
class practice2
{
    public static void main(String args[])
    {
        // Write a program to reverse the elements of array
        // int arr[] = {3, 1, 3, 2, 1, 3, 4, 2, 1};
        // List<Integer> li = new ArrayList<>();
        
        Integer arr[] = {3, 4, 6, 5, 7}; // same as int but Integer is a class
        List<Integer> li = Arrays.asList(arr);
        Collections.reverse(li);
        System.out.println(li);
        // System.out.println(arr[0]);
        for(int i : arr)
        {
            System.out.print(i + " ");
        }
    }
}