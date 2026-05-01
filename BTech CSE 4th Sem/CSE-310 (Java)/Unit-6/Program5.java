import java.util.*;

public class Program5 {
    public static void main(String args[])
    {
        Integer arr1 [] = {1, 2, 3, 4, 5};
        Integer arr2 [] = {3, 4, 6};

        ArrayList<Integer> li1 = new ArrayList<>(Arrays.asList(arr1));
        ArrayList<Integer> li2 = new ArrayList<>(Arrays.asList(arr2));
        li1.addAll(li2);
        Collections.sort(li1);
        ArrayList<Integer> result = new ArrayList<>();
        for(int i : li1)
        {
            if(!result.contains(i))
            {
                result.add(i);
            }
        }
        System.out.println(result);
    }
}
