import java.util.*;
class caProgram1
{
    // Write a program to find the occurance of every element from an array
    public static void main(String args[])
    {
        int arr[] = {3, 2, 1, 2, 3, 1, 4, 2, 3, 3};
        int max = arr[0];
        for(int i = 1; i < arr.length; i++)
        {
            if(arr[i] > max)
            {
                max = arr[i];
            }
        }
        int block[] = new int[max + 1];
        for(int i = 0; i < arr.length; i++)
        {
            block[arr[i]]++; 
        }
        Set<Integer> f = new LinkedHashSet<>();
        for(int i = 0; i < arr.length; i++)
        {
            f.add(arr[i]);
        }
        for(int i : f)
        {
            System.out.println(i + " present " + block[i]);
        }
    }
}