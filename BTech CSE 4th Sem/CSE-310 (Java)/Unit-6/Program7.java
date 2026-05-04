/*
    Write a program to move all zeroes to the right side of an array list
*/
import java.util.*;

class Program7
{
    public static void main(String args[])
    {
        Integer arr[] = {1, 0, 2, 5, 0, 7, 3, 0};
        ArrayList<Integer> a = new ArrayList<>(Arrays.asList(arr));
        ArrayList<Integer> result = new ArrayList<>();
        for(Integer val : a)
        {
            if(val != 0)
            {
                result.add(val);
            }
        }
        while(result.size() != a.size())
        {
            result.add(0);
        }
        System.out.println(result);
    }
}