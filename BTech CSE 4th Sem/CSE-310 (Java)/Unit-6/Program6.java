import java.util.*;

public class Program6 {
    public static void main(String args[])
    {
        Integer arr1 [] = {1, 2, 3, 4, 5};
        ArrayList<Integer> li1 = new ArrayList<>(Arrays.asList(arr1));
       
        int k = 2;

        for(int i = 0; i < k; i++)
        {
            int no = li1.remove(li1.size() -1);
            li1.add(0, no);
        }
        // Collections.rotate(li1, k);
        System.out.println(li1);
    }
}
