import java.util.*;
class collectionSets
{
    public static void main(String args[])
    {
        // Won't include duplicate elements
        Set<Integer> st = new HashSet<>();
        // Output is not sorted. cross check.
        st.add(40);
        st.add(20);
        st.add(30);
        st.add(10);
        System.out.println(st);
    }
}