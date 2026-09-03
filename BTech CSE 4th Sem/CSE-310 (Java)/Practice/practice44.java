public class practice44 {
    static void add(int a, int b)
    {
        a = a + 10;
        b = b + 10;
        System.out.println("a in (add): " + a);
        System.out.println("b in (add): " + b);
    }
    public static void main(String args[])
    {
        int a = 10, b = 20;
        add(10, 20);
        System.out.println("a : " + a);
        System.out.println("b : " + b);
    }
}
