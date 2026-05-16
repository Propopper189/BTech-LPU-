import java.util.*;
public class practice53 {
    public static void main(String args[])
    {
        Deque<Integer> dq = new ArrayDeque<>();
        dq.addFirst(10);
        dq.addLast(20);
        dq.addFirst(11);
        for(Integer i : dq)
        {
            System.out.println(i);
        }
        Deque<Integer> dq1 = new ArrayDeque<>(dq);
        System.out.println("Elements in dq1 from back to front :");
        while(!dq1.isEmpty())
        {
            System.out.println(dq1.getLast());
            dq1.removeLast();
        }
        System.out.println("Peek First Element In dq : " + dq.peekFirst());
        System.out.println("Peek Last element in dq : " + dq.peekLast());

    }
}
