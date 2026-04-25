import java.util.*;
class reverseArray
{
    public static void main(String args[])
    {
        int arr[] = {3, 2, 5, 4, 7, 6};
        int i = 0, j = arr.length-1;
        while(i < j)
        {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
        System.out.println(Arrays.toString(arr));
    }
}