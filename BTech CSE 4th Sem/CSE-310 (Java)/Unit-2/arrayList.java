/*
Collections
1) List
2) Set
3) Map

Declare a List
------------------------------------
List<Intger> li = new ArrayList<>();
li.add(10);
li.add(20);
li.add(30);
li.add(40);
System.out.println(li.size());
*/
import java.util.*;

class arrayList // ArrayList
{
    public static void main(String args[])
    {
        List<Integer> li = new ArrayList<>();
        li.add(10);
        li.add(20);
        li.add(30);
        li.add(40);
        System.out.println(li.size());
        System.out.println(li);
        li.add(1, 15);
        System.out.println(li);
        li.remove(3);
        System.out.println(li);
        System.out.println(li.isEmpty());
        System.out.println(li.contains(15));
        Collections.reverse(li);
        System.out.println(li);
    }
}