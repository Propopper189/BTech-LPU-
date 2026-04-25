import java.util.*;
class array4
{
    // how to find the length of the array
    public static void main(String args[])
    {
        int b[] = {2, 1, 3, 5, 4};
        System.out.println(b.length); // without paranthesis
        // how to find length of string.
        String s = "lpu";
        System.out.println(s.length()); // paranthesis

        // print all elements of array
        for(int i = 0; i < b.length; i++)
        {
            System.out.print(b[i] + " ");
        }
        System.out.println();
        // print all elements of array in one line
        System.out.println(Arrays.toString(b));
        // Sort the arrays
        Arrays.sort(b);
        System.out.println(Arrays.toString(b));
        // Search the element in sorted array
        System.out.println(Arrays.binarySearch(b, 3));
    }
}