import java.util.*;
public class practice47 
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);    
        ArrayList<String> l1 = new ArrayList<>();
        int n = sc.nextInt();
        for(int i = 0; i < n; i++)
        {
            l1.add(sc.next());
        }
        Collections.sort(l1);
        l1.remove(0);
        for(String s : l1)
        {
            System.out.println(s);
        }
        System.out.println(l1.size());
        // System.out.println(l1.get(0));
        l1.set(0, "Aquib");
        for(String s : l1)
        {
            System.out.println(s);
        }
    }
}
