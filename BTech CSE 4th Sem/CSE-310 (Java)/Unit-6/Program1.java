/*
    Convert array to ArrayList.
*/
import java.util.*;
class Program1
{
    public static void main(String args[])
    {
        // First Method
        int arr[] = {2, 7, 3, 5, 4};
        ArrayList<Integer> li = new ArrayList<>();
        for(int j : arr)
        {
            li.add(j);
        }
        System.out.println("Before Reversal : ");
        System.out.println(Arrays.toString(arr));
        System.out.println(li);
        Collections.reverse(li);
        System.out.println("After Reversal : ");
        System.out.println(li);

        // Second Method
        System.out.println("Second Method : ");
        Integer arr2[] = {3, 5, 4, 7, 6};
        ArrayList<Integer> li2 = new ArrayList<>(Arrays.asList(arr2));
        System.out.println(li2);
    }
}