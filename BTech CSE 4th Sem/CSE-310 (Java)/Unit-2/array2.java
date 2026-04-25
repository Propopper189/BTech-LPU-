import java.util.*;
class array2
{
    public static void main(String args[])
    {
        int arr[] = new int[5];
        Arrays.fill(arr, -1); // Arrays class present inside util.
        // every element inside the array is filled by -1;
        for(int i = 0; i < 5; i++)
        {
            System.out.println(arr[i]);
        }
    }
}